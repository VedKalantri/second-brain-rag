import os
from dotenv import load_dotenv
import google.generativeai as genai

from search import search_notes

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def build_context(results):
    """
    Combine retrieved chunks into one context string.
    """

    context = ""

    for i, doc in enumerate(results["documents"][0]):

        context += f"\nChunk {i+1}:\n"
        context += doc
        context += "\n"

    return context


print("=" * 60)
print("🧠 Second Brain")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    results = search_notes(question)

    context = build_context(results)

    prompt = f"""
You are my personal Second Brain.

Answer ONLY using the context below.

If the answer is not found in the notes, reply exactly:

"I couldn't find that information in your notes."

Context:
--------------------
{context}
--------------------

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    print("\nSecond Brain:\n")
    print(response.text)

    print("\n" + "=" * 60)
print("📚 Sources Used")
print("=" * 60)

for i in range(len(results["documents"][0])):

    metadata = results["metadatas"][0][i]
    distance = results["distances"][0][i]

    if metadata is not None:

        print(
            f"Chunk {metadata['chunk_number']} "
            f"(Distance: {distance:.4f})"
        )