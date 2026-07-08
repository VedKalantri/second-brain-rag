from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

sentence1 = "Docker Compose manages multiple containers."

sentence2 = "How can I run multiple Docker containers?"

sentence3 = "The Eiffel Tower is located in Paris."

emb1 = model.encode(sentence1)
emb2 = model.encode(sentence2)
emb3 = model.encode(sentence3)

print("Docker vs Docker:",
      cos_sim(emb1, emb2).item())

print("Docker vs Pizza:",
      cos_sim(emb1, emb3).item())