
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def query_gemini(prompt: str) -> str:
    """
    Sends a prompt to Gemini-2.5-flash and returns the response text using google-generativeai client.
    """
    model = genai.GenerativeModel('models/gemini-2.5-flash')
    response = model.generate_content(prompt)
    # Extract the generated text from the response
    try:
        return response.text
    except Exception:
        return str(response)

# Example usage:
# print(query_gemini("Hello Gemini!"))
