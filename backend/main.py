
import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

# --- LangChain Imports ---
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter

# --- Local Imports ---
from vector_store import get_vector_store, ingest_text, get_env_variable
from database import get_db, init_db, User
from auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    get_current_user
)

# --- Environment and App Setup ---
load_dotenv()
app = FastAPI(
    title="RAG Chatbot Backend",
    description="A FastAPI backend for a RAG chatbot using LangChain, Qdrant, and Neon.",
    version="0.1.0",
)

# --- CORS Configuration ---
# WARNING: This is a permissive CORS configuration for development.
# For production, restrict the origins to your frontend's domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# --- Pydantic Models for Request/Response ---
class IngestRequest(BaseModel):
    collection_name: str
    content: str

class ChatRequest(BaseModel):
    collection_name: str
    question: str

class ChatSelectionRequest(BaseModel):
    question: str
    selected_text: str

class ChatResponse(BaseModel):
    answer: str

# --- Authentication Models ---
class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    username: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

class GoogleLoginRequest(BaseModel):
    token: str

# --- LangChain RAG Setup ---
# Initialize the LLM with Groq
try:
    GROQ_API_KEY = get_env_variable("GROQ_API_KEY")
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY,
        temperature=0.3,
        max_tokens=150
    )
except ValueError as e:
    print(f"LLM Initialization Error: {e}")
    llm = None # Handle case where API key is not set

# --- API Endpoints ---
@app.post("/ingest", status_code=201)
async def ingest_endpoint(file: UploadFile = File(...), collection_name: str = Body(...)):
    """
    Endpoint to ingest a text file. It reads the file, splits it into chunks,
    and stores the embeddings in the specified Qdrant collection.
    """
    try:
        content = await file.read()
        text = content.decode("utf-8")
        
        if not text.strip():
            raise HTTPException(status_code=400, detail="File is empty or contains only whitespace.")

        ingest_text(text=text, collection_name=collection_name)
        return {"message": f"Successfully ingested file '{file.filename}' into collection '{collection_name}'."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to ingest file: {str(e)}")

def create_rag_chain(collection_name: str):
    """Helper function to create a RAG chain for a given collection."""
    if not llm:
        raise HTTPException(status_code=500, detail="LLM not initialized. Check GROQ_API_KEY.")

    try:
        vector_store = get_vector_store(collection_name)
        retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vector store error: {str(e)}")

    # This prompt instructs the AI to ONLY use the context.
    # If the answer is not in the context, it should say so.
    template = """
You are an AI assistant for a book on Physical AI and Humanoid Robotics.
Answer the question based ONLY on the context provided.
If the context does not contain the answer, you MUST respond with the exact phrase: "The answer is not in the book."
Do not add any other words or explanation.

Context:
{context}

Question:
{question}

Answer:
"""

    prompt = ChatPromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

async def get_general_response(question: str) -> str:
    """Invokes a general-purpose LLM for real-time answers."""
    if not llm:
        raise HTTPException(status_code=500, detail="LLM not initialized.")
    
    template = """You are a helpful AI assistant (like ChatGPT). 
Answer the following question conversationally and naturally.

Question: {question}

Answer:
"""
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"question": question})

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Handles chat requests by first consulting the book (RAG) and then falling back to a general LLM.
    """
    try:
        # Always try the RAG chain first
        rag_chain = create_rag_chain(request.collection_name)
        rag_answer = rag_chain.invoke(request.question)

        # If the RAG chain says the answer isn't in the book, get a general response
        if "not in the book" in rag_answer.lower():
            # Before getting a real-time answer, check if the user is asking for it.
            # This handles the "Would you like me to search..." response from the RAG chain.
            # For now, we will assume the user always wants a real-time answer if the book doesn't have it.
            # A more advanced implementation would require state management.
            
            # Let's re-ask the LLM for a public answer without the book context
            print("Answer not found in the book, getting a real-time response...")
            general_answer = await get_general_response(request.question)
            return ChatResponse(answer=general_answer)

        # Otherwise, return the answer from the book
        return ChatResponse(answer=rag_answer)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process chat request: {str(e)}")

@app.post("/chat-selection", response_model=ChatResponse)
async def chat_selection_endpoint(request: ChatSelectionRequest):
    """
    Endpoint for asking questions based on user-selected text.
    This bypasses the retriever and uses the provided text as context.
    """
    if not llm:
        raise HTTPException(status_code=500, detail="LLM not initialized. Check OPENAI_API_KEY.")

    template = """
    You are an assistant for question-answering tasks. 
    Use ONLY the following context to answer the question. 
    If the answer cannot be found in the context, just say that you don't know.

    Context: {context} 

    Question: {question} 

    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Here we create a simple chain that uses the provided text directly
    chain = (
        prompt
        | llm
        | StrOutputParser()
    )
    
    try:
        answer = chain.invoke({"context": request.selected_text, "question": request.question})
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process chat request: {str(e)}")


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to the RAG Chatbot Backend. Visit /docs for the API documentation."}

# --- Authentication Endpoints ---
@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_db()
    print("Database initialized successfully")

@app.post("/auth/signup", response_model=TokenResponse, status_code=201)
async def signup(request: SignupRequest, db: Session = Depends(get_db)):
    """
    Register a new user
    """
    # Check if username already exists
    existing_user = db.query(User).filter(User.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Check if email already exists
    existing_email = db.query(User).filter(User.email == request.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    hashed_password = get_password_hash(request.password)
    new_user = User(
        username=request.username,
        email=request.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create access token
    access_token = create_access_token(data={"sub": new_user.username})

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        username=new_user.username
    )

@app.post("/auth/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    """
    Login user and return access token
    """
    # Find user by username
    user = db.query(User).filter(User.username == request.username).first()

    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )

    # Create access token
    access_token = create_access_token(data={"sub": user.username})

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        username=user.username
    )

@app.get("/auth/me", response_model=UserResponse)
async def get_me(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    Get current logged-in user information
    """
    user = db.query(User).filter(User.username == current_user["username"]).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email
    )

@app.post("/auth/google", response_model=TokenResponse)
async def google_login(request: GoogleLoginRequest, db: Session = Depends(get_db)):
    """
    Login or signup using Google OAuth token
    """
    try:
        # Get Google Client ID from environment
        GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

        if not GOOGLE_CLIENT_ID:
            raise HTTPException(status_code=500, detail="Google OAuth not configured")

        # Verify the Google token
        idinfo = id_token.verify_oauth2_token(
            request.token,
            google_requests.Request(),
            GOOGLE_CLIENT_ID
        )

        # Get user info from Google token
        google_user_id = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name', email.split('@')[0])

        # Check if user exists
        user = db.query(User).filter(User.email == email).first()

        if not user:
            # Create new user with Google info
            username = email.split('@')[0] + '_' + google_user_id[:8]

            # Generate a random password (user won't use it for Google login)
            random_password = get_password_hash(os.urandom(32).hex())

            user = User(
                username=username,
                email=email,
                hashed_password=random_password
            )
            db.add(user)
            db.commit()
            db.refresh(user)

        # Create access token
        access_token = create_access_token(data={"sub": user.username})

        return TokenResponse(
            access_token=access_token,
            token_type="bearer",
            username=user.username
        )

    except ValueError as e:
        # Invalid token
        raise HTTPException(status_code=401, detail="Invalid Google token")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Google authentication failed: {str(e)}")

if __name__ == "__main__":
    # To run this server:
    # 1. Ensure you have a .env file with your API keys.
    # 2. In your terminal, navigate to the 'backend' directory.
    # 3. Activate the virtual environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
    # 4. Install dependencies: `pip install -r requirements.txt`
    # 5. Run the server: `uvicorn main:app --reload`
    print("Starting FastAPI server...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

@app.post("/chat-general", response_model=ChatResponse)
async def chat_general_endpoint(request: ChatRequest):
    """
    General chat endpoint without RAG - for greetings and general questions
    """
    if not llm:
        raise HTTPException(status_code=500, detail="LLM not initialized.")

    try:
        # Simple prompt for general conversation
        template = """You are a friendly AI assistant specialized in Physical AI and Humanoid Robotics.
        
The user said: {question}

Respond naturally and helpfully. If it's a greeting, greet them back warmly. 
If they ask about Physical AI or robotics, provide helpful information.
If they ask general questions, answer them conversationally."""

        prompt = ChatPromptTemplate.from_template(template)
        
        chain = prompt | llm | StrOutputParser()
        answer = chain.invoke({"question": request.question})
        
        return ChatResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process request: {str(e)}")
