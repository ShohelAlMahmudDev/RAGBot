import os
import faiss
import pickle
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from fastapi.middleware.cors import CORSMiddleware
from worker import process_message

# Load model & FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")


# Get the base directory dynamically (cross-platform)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database", "faiss_index.pkl")  # Cross-platform path
# Serve static files (CSS, JS, images)
STATIC_DIR = os.path.join(BASE_DIR, "static")


# Serve templates
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)



def load_index():
    if not os.path.exists(DB_PATH):  # Ensure file exists
        raise FileNotFoundError(f"File not found: {DB_PATH}")
    
    with open(DB_PATH, "rb") as f:
        data = pickle.load(f)

    #print(f"Loaded data type: {type(data)}")  # Debugging: Check the data structure
    return data


faiss_index, texts = load_index()

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
def ask_question(query: Query):
    """Search FAISS index for the best answer to a question."""
    question_embedding = model.encode(query.question).reshape(1, -1)

    # Search for the most relevant chunk
    D, I = faiss_index.search(question_embedding, k=3)
    best_matches = [texts[i] for i in I[0]]
    #print(best_matches)
    #return {"answers": best_matches}
    processed_msg=process_message(best_matches,query.question) 
    return  {"answers": processed_msg}
    #return process_message(best_matches,query.question) 

@app.post("/reload")
def reload_index():
    """Reload the FAISS index after updating."""
    global faiss_index, texts
    faiss_index, texts = load_index()
    return {"status": "Index reloaded successfully!"}
