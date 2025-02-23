import requests

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API keys 

TOGETHER_API_KEY=os.getenv("TOGETHER_API_KEY")
TOGETHER_API_SERVICE_URL = os.getenv("TOGETHER_API_SERVICE_URL")

def process_message(context,user_message):
     
    prompt = f"""
You are an expert AI assistant but you will act as Software Engineer and Your name is Shohel Al Mahmud  as trained on the given context.  
Answer accurately, concisely, and in a professional tone. if user ask for private information(address,phone,Living info) provide my email address and ask to send an email for more information. 
If the context lacks information, say "I don't have enough data to answer. "

Context:
{context}

Question: {user_message}

Response:
"""

    # Call the OpenAI API to process the prompt
    try: 
        MODEL = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
        headers = {
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message}
                ],
        }

        # Debug the request payload and headers
        response = requests.post(TOGETHER_API_SERVICE_URL, json=data, headers=headers)

        # Parse the response
        response_json = response.json()
        if "choices" in response_json and len(response_json["choices"]) > 0:
            response_text = response_json["choices"][0]["message"]["content"]
            return response_text
        else:
            print("Unexpected response format:", response_json)
            return None

    except requests.exceptions.RequestException as e:
        print("Error during TOGETHER API request:", e)
        return None