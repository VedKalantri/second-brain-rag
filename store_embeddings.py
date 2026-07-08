import chromadb
from sentence_transformers import SentenceTransformer
from chunk_notes import get_chunks

# Load embedding model
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

# Create/Open ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="second_brain"
)

# Get chunks
chunks = get_chunks()

print(f"Found {len(chunks)} chunks\n")

for i, chunk in enumerate(chunks):

    embedding = model.encode(chunk).tolist()

    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding],
        metadatas=[
            {
                "chunk_number": i + 1,
                "source": "Notion Page"
            }
        ]
    )

print("✅ All chunks stored successfully!\n")

# Verify everything
results = collection.get(
    include=["documents", "metadatas"]
)

print("=" * 60)

for i in range(len(results["ids"])):

    print(f"ID: {results['ids'][i]}")

    print("Metadata:", results["metadatas"][i])

    print("Document:")

    print(results["documents"][i])

    print("-" * 60)