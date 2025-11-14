from sentence_transformers import SentenceTransformer, util
from langchain_ollama import OllamaEmbeddings
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
# model = OllamaEmbeddings(model="llama3.2")

texts = ["Apple iPhone 15", "Samsung Galaxy S24", "MacBook Pro M3", "Dell XPS 15", "Mango fruit", "Banana"]

embeddings = model.encode(texts, normalize_embeddings=True)

# Compute pairwise similarities
for i, t1 in enumerate(texts):
    for j, t2 in enumerate(texts):
        if i < j:
            sim = np.dot(embeddings[i], embeddings[j])
            print(f"{t1} vs {t2} → similarity {sim:.2f}")
