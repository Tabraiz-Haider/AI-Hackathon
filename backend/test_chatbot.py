"""
Simple test script for the RAG chatbot
"""
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize components
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

print("Initializing LLM...")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0.7
)

print("Initializing Embeddings...")
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

print("Connecting to Qdrant...")
vector_store = QdrantVectorStore.from_existing_collection(
    collection_name="test_collection",
    embedding=embeddings,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

print("Creating retriever...")
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

print("Setting up RAG chain...")
template = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Keep the answer concise.

Context: {context}

Question: {question}

Answer:"""

prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print("\n" + "="*50)
print("RAG Chatbot Ready!")
print("="*50 + "\n")

# Test question
question = "What is Physical AI?"
print(f"Question: {question}\n")

try:
    answer = rag_chain.invoke(question)
    print(f"Answer: {answer}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
