"""
Script to create Qdrant collection
"""
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from dotenv import load_dotenv
import os

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "test_collection"

# Initialize Qdrant client
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

print(f"Connected to Qdrant at {QDRANT_URL}")

# Check if collection exists
collections = client.get_collections()
collection_names = [col.name for col in collections.collections]

if COLLECTION_NAME in collection_names:
    print(f"Collection '{COLLECTION_NAME}' already exists!")
else:
    # Create collection
    # OpenAI text-embedding-3-small uses 1536 dimensions
    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )
    print(f"Collection '{COLLECTION_NAME}' created successfully!")

# List all collections
print("\nAvailable collections:")
for col in collections.collections:
    print(f"  - {col.name}")
