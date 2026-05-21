from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class RAGEngine:
    def __init__(self, file_path):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.chunks = self.load_and_split(file_path)
        self.index = self.create_faiss_index()

    def load_and_split(self, file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Simple chunking
        chunks = text.split("\n\n")
        return [c.strip() for c in chunks if len(c.strip()) > 50]

    def create_faiss_index(self):
        embeddings = self.model.encode(self.chunks)
        dim = embeddings.shape[1]

        index = faiss.IndexFlatL2(dim)
        index.add(np.array(embeddings))
        self.embeddings = embeddings

        return index

    def query(self, question, k=3):
        q_emb = self.model.encode([question])
        distances, indices = self.index.search(np.array(q_emb), k)

        results = [self.chunks[i] for i in indices[0]]
        return "\n\n".join(results)