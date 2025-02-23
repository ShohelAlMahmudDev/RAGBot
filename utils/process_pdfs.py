import os
import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import pickle

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def process_pdfs(pdf_folder):
    """Process all PDFs in a folder, create embeddings, and save to FAISS index."""
    texts = []
    embeddings = []

    # Process each PDF in the folder
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, filename)
            print(f"Processing: {filename}")
            text = extract_text_from_pdf(pdf_path)

            # Split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = text_splitter.split_text(text)

            # Create embeddings for each chunk
            chunk_embeddings = [model.encode(chunk) for chunk in chunks]

            texts.extend(chunks)
            embeddings.extend(chunk_embeddings)

    # Convert to numpy array
    embeddings = np.array(embeddings)

    # Create FAISS index
    dimension = embeddings.shape[1]
    faiss_index = faiss.IndexFlatL2(dimension)
    faiss_index.add(embeddings)

    # Save FAISS index and texts
    with open("faiss_index.pkl", "wb") as f:
        pickle.dump((faiss_index, texts), f)

    print("Embeddings stored successfully!")

if __name__ == "__main__":
    pdf_folder = "docs"  # Folder containing multiple PDFs
    process_pdfs(pdf_folder)
