from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

texts = [
    "Docker is a container platform.",
    "Docker helps run containers.",
    "I love eating pizza."
]

for text in texts:
    embedding = model.encode(text)
    print("Embedding length:", len(embedding))
    print("\nFirst 10 values:")
    print(embedding[:10])

    print("-" * 40)
# Generate embedding


