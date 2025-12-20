
import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load environment variables from .env file
load_dotenv()

# Environment variable validation
def get_env_variable(var_name: str) -> str:
    """Gets an environment variable or raises an error if it's not set."""
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' not set. Please add it to the .env file.")
    return value

# Load API keys and URLs
OPENROUTER_API_KEY = get_env_variable("OPENROUTER_API_KEY")
QDRANT_URL = get_env_variable("QDRANT_URL")
QDRANT_API_KEY = get_env_variable("QDRANT_API_KEY")

# --- Qdrant Client Initialization ---
def get_qdrant_client() -> QdrantClient:
    """Initializes and returns the Qdrant client."""
    return QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        timeout=60.0,
    )

# --- Embeddings Model ---
def get_embeddings_model() -> OpenAIEmbeddings:
    """Initializes and returns the OpenAI embeddings model via OpenRouter."""
    return OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

# --- Text Splitting ---
def get_text_splitter(chunk_size: int = 1000, chunk_overlap: int = 200) -> RecursiveCharacterTextSplitter:
    """Creates and returns a text splitter."""
    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

# --- Vector Store Logic ---
def get_vector_store(collection_name: str) -> QdrantVectorStore:
    """
    Initializes a Qdrant vector store.
    If the collection doesn't exist, it will be created automatically.
    """
    embeddings = get_embeddings_model()

    vector_store = QdrantVectorStore.from_existing_collection(
        collection_name=collection_name,
        embedding=embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )
    return vector_store

def get_collection_info(collection_name: str) -> dict:
    """Gets information about a Qdrant collection."""
    qdrant_client = get_qdrant_client()
    try:
        # Use the new API to get collection info
        collection_info = qdrant_client.get_collection(collection_name=collection_name)
        # Extract the point count from the new response structure
        points_count = collection_info.points_count if hasattr(collection_info, 'points_count') else 0
        return {
            "points_count": points_count,
        }
    except Exception as e:
        # Handle cases where the collection does not exist
        if "404" in str(e) or "Not found" in str(e): # Handle not found case
            return {"points_count": 0}
        print(f"An error occurred while getting collection info: {e}")
        return {}


def ingest_text(text: str, collection_name: str):
    """
    Splits text, creates embeddings, and upserts them into a Qdrant collection.
    """
    text_splitter = get_text_splitter()
    documents = text_splitter.create_documents([text])
    
    vector_store = get_vector_store(collection_name)
    vector_store.add_documents(documents)
    print(f"Successfully ingested text into collection '{collection_name}'.")

def load_all_chapters():
    """
    Reads all chapter markdown files and returns their content as a combined string.
    """
    import glob

    # Get all markdown files from docs/my-book directory
    book_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'my-book')
    chapter_files = sorted(glob.glob(os.path.join(book_path, '*.md')))

    all_content = []

    for file_path in chapter_files:
        filename = os.path.basename(file_path)
        print(f"Reading {filename}...")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Add chapter metadata
                all_content.append(f"\n\n--- FILE: {filename} ---\n\n")
                all_content.append(content)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    combined_content = '\n'.join(all_content)
    print(f"\nTotal content length: {len(combined_content)} characters")
    return combined_content

def ingest_all_book_content(collection_name: str = "physical_ai_robotics_book"):
    """
    Loads all chapter content and ingests it into Qdrant vector store.
    This function will delete the collection if it already exists to ensure a fresh start.
    """
    print("=" * 60)
    print("Starting Book Content Ingestion Process")
    print("=" * 60)

    qdrant_client = get_qdrant_client()
    
    # Check if collection exists and delete it
    print(f"\n0. Checking for existing collection '{collection_name}'...")
    try:
        # Correctly check for collection existence
        collections_response = qdrant_client.get_collections()
        # The response is a tuple/list-like object, so we need to iterate or check properly
        existing_collections = [c.name for c in collections_response.collections]
        if collection_name in existing_collections:
            print(f"Collection '{collection_name}' already exists. Deleting it to ensure a fresh start.")
            qdrant_client.delete_collection(collection_name=collection_name)
            print(f"Collection '{collection_name}' deleted.")
        else:
            print(f"Collection '{collection_name}' does not exist. A new one will be created.")
    except Exception as e:
        print(f"An error occurred while checking/deleting the collection: {e}")
        # Decide if you want to proceed or stop
        return


    # Load all chapters
    print("\n1. Loading all chapter content...")
    book_content = load_all_chapters()

    # Split into chunks
    print("\n2. Splitting text into chunks...")
    text_splitter = get_text_splitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.create_documents([book_content])
    print(f"Created {len(documents)} document chunks")

    # Initialize embeddings and vector store
    print("\n3. Initializing embeddings and vector store...")
    embeddings = get_embeddings_model()
    
    # Create new collection and ingest documents
    print(f"\n4. Creating and populating collection '{collection_name}'...")
    
    # Use from_documents which handles creation and ingestion
    vector_store = QdrantVectorStore.from_documents(
        documents,
        embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=collection_name,
        batch_size=32, # Adjusted batch size
        force_recreate=True, # Ensures collection is recreated
    )

    print("\n" + "=" * 60)
    print("SUCCESS: All book content ingested!")
    print(f"Collection: {collection_name}")
    
    # Verify the number of points in the collection
    final_info = get_collection_info(collection_name)
    final_points_count = final_info.get('points_count', 'N/A')
    print(f"Total chunks in collection: {final_points_count}")
    print("=" * 60)


if __name__ == '__main__':
    collection_name = "physical_ai_robotics_book"
    
    # 1. Check initial state of the collection
    print("--- Checking initial state of the Qdrant collection ---")
    initial_info = get_collection_info(collection_name)
    initial_points_count = initial_info.get('points_count', 'N/A')
    print(f"Collection '{collection_name}' currently has {initial_points_count} points.")
    print("-" * 55)

    # 2. Ingest all book content
    try:
        ingest_all_book_content(collection_name)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
        
    # 3. Verify final state of the collection
    print("\n--- Verifying final state of the Qdrant collection ---")
    final_info = get_collection_info(collection_name)
    final_points_count = final_info.get('points_count', 'N/A')
    print(f"Collection '{collection_name}' now has {final_points_count} points.")
    print("-" * 55)
