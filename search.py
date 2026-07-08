import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="second_brain"
)


def search_notes(query, n_results=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    return results


if __name__ == "__main__":

    question = input("Ask your Second Brain: ")

    results = search_notes(question)

    print("\n")

    for i in range(len(results["documents"][0])):

        print("=" * 60)

        print(f"Rank : {i+1}")

        print(f"Distance : {results['distances'][0][i]:.4f}")

        print(f"Metadata : {results['metadatas'][0][i]}")

        print()

        print(results["documents"][0][i])

        print()