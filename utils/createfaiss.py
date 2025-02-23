import faiss
import pickle
from sentence_transformers import SentenceTransformer

def create_faiss_index(texts):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    # Save index
    with open("faiss_index.pkl", "wb") as f:
        pickle.dump((index, texts), f)

    print("FAISS index created and saved.")

# Example texts (Replace with actual text extraction from PDFs)
texts = ["This is a sample document.", "Another document for testing."]
create_faiss_index(texts)
