# RAGBot: Personalized AI Chatbot

RAGBot is an innovative AI chatbot designed to simulate a Software Engineer’s Profile. By utilizing profile data, RAGBot provides personalized, technical, and career-focused Information. The chatbot leverages advanced natural language processing techniques combined with retrieval-augmented generation to generate context-aware responses.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Overview
RAGBot brings together modern frontend and backend technologies to deliver a seamless, engaging chatbot experience. With a user-friendly interface built using HTML5, CSS, JavaScript, and Bootstrap, and a powerful backend powered by FastAPI and a suite of AI libraries, RAGBot is designed for anyone looking to get to know about me can ask to my chatbot.

## Features
- **Personalized Responses:** Tailors answers based on the user’s profile data.
- **Advanced Query Processing:** Uses state-of-the-art retrieval and generation techniques.
- **Technical Guidance:** Acts as a virtual Software Engineer to answer about the personalized skills and profile related questions.
- **Responsive Frontend:** Developed with HTML5, CSS, JavaScript, and Bootstrap for a modern UI.
- **Robust Backend:** Powered by FastAPI, Uvicorn, and AI libraries such as Sentence Transformers, FAISS, LangChain, and pypdf.
- **Easy Configuration:** Environment-specific settings are managed through dotenv.

## Architecture
RAGBot is structured into two primary layers:

### Frontend
- **Technologies:** HTML5, CSS, JavaScript, Bootstrap.
- **Role:** Provides a responsive and interactive interface for users to enter their profile data and queries.

### Backend
- **Framework:** FastAPI (with Uvicorn as the ASGI server).
- **Libraries & Tools:**
  - **Sentence Transformers & FAISS:** For generating text embeddings and efficient similarity searches.
  - **LangChain:** To orchestrate the flow of data and model interactions.
  - **pypdf:** For processing PDF documents when needed.
  - **dotenv:** For managing environment variables and configuration.
- **Flow Diagram:**

```
      +---------------------------------------------------+
      |                                                   |
      |      Frontend (HTML5, CSS, JS, Bootstrap)         |
      |  – User Interface for input & display            |
      +--------------------+------------------------------+
                           |
                           | HTTP API Calls
                           v
      +--------------------------------------------+
      |           Backend (FastAPI & Uvicorn)      |
      |  - Receives requests and fetches profile    |
      |    data                                     |
      |  - Processes queries using AI libraries     |
      +--------------------+-----------------------+
                           |
                           | AI Processing Flow:
                           | Sentence Transformers, FAISS,
                           | LangChain, pypdf, etc.
                           v
      +--------------------------------------------+
      |    Personalized AI Response Generation     |
      +--------------------------------------------+
```

## Installation

### Prerequisites
- **Python 3.8+**
- **pip** (Python package manager)
- **Git** (for repository cloning)

### Step 1: Clone the Repository
Clone the repository to your local machine via:
```bash
git clone https://github.com/ShohelAlMahmudDev/RAGBot.git
cd RAGBot
```

### Step 2: Install Python Dependencies
Install the required dependencies. Ensure you have a virtual environment activated, then run:
```bash
pip install -r requirements.txt
```
*following are the packages in `requirements.txt`, need to be installed:*
```
fastapi
uvicorn
sentence-transformers
faiss-cpu
pypdf
langchain
python-dotenv
```

### Frontend Setup
The frontend is built from static files. These can be served by Python backend. No additional build steps are needed.

## Configuration
RAGBot uses environment variables to manage API keys, model configurations, and paths to profile data. Create a `.env` file in the root directory with settings similar to:
```
# .env file
TOGETHER_API_KEY=""
TOGETHER_API_SERVICE_URL=""
```

## Usage

### Running the Backend Server
Start the FastAPI server using Uvicorn:
```Console/Terminal
uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```
This command runs the server in development mode with automatic code reloading.

### Interacting with RAGBot
- **Access the Frontend:** Open your browser and navigate to `http://localhost:8000` (or the appropriate URL if hosted differently) to interact with the chatbot.
- **API Documentation:** Visit `http://localhost:8000/docs` to explore the interactive API documentation provided by FastAPI.

Once launched, input your profile data and ask your questions. RAGBot will process the input using its retrieval-augmented generation engine and return a personalized response.



## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions, suggestions, or contributions, please reach out:
- **Project Maintainer:** [ShohelAlMahmudDev](https://github.com/ShohelAlMahmudDev)
- **Email:** shohelcse@yahoo.com
```
