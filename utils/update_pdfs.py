import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def update_pdfs(pdf_folder):
    """Add new PDFs to the existing FAISS index."""
    with open("faiss_index.pkl", "rb") as f:
        faiss_index, texts = pickle.load(f)

    new_texts = []
    new_embeddings = []

    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            print(f"Updating with: {filename}")
            text = extract_text_from_pdf(pdf_path)

            # Split text
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = text_splitter.split_text(text)

            # Embeddings
            chunk_embeddings = [model.encode(chunk) for chunk in chunks]

            new_texts.extend(chunks)
            new_embeddings.extend(chunk_embeddings)

    # Add new embeddings to FAISS
    new_embeddings = np.array(new_embeddings)
    faiss_index.add(new_embeddings)
    texts.extend(new_texts)

    # Save updated index
    with open("faiss_index.pkl", "wb") as f:
        pickle.dump((faiss_index, texts), f)

    print("FAISS index updated successfully!")

if __name__ == "__main__":
    pdf_folder = "newdocs"
    update_pdfs(pdf_folder)
