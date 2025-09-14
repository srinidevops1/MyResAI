import os
import speech_recognition as sr
import requests  # New import for making HTTP requests
from dotenv import load_dotenv
from sarvamai import SarvamAI

import tempfile
from gemini_integration import query_gemini

# Load environment variables from .env file
load_dotenv()

def get_api_keys():
    """
    Retrieves API keys from environment variables.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    sarvam_api_key = os.getenv("SARVAM_API_KEY")
    
    if not sarvam_api_key:
        raise ValueError("SARVAM_API_KEY not found in .env file")
        
    return gemini_api_key, sarvam_api_key

def listen_for_telugu_speech():
    """
    Listens for audio from the microphone and saves it to a temporary file.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak in Telugu.")
        audio = r.listen(source)
        print("Finished listening.")

    try:
        # Create a temporary file to save the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
            fp.write(audio.get_wav_data())
            return fp.name
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def transcribe_telugu_speech(audio_file_path, sarvam_api_key):
    """
    Transcribes Telugu audio from a file using Sarvam AI.
    """
    if not audio_file_path:
        return None
        
    try:
        client = SarvamAI(api_subscription_key=sarvam_api_key)
        
        with open(audio_file_path, "rb") as audio_file:
            response = client.speech_to_text.transcribe(
                file=audio_file,
                model="saarika:v2.5", # Using a model specified in Sarvam AI docs
                language_code="te-IN"  # Telugu
            )
        
        # Clean up the temporary file
        os.remove(audio_file_path)
        
        # Corrected: Use the 'transcript' attribute
        return response.transcript

    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        # Clean up the temporary file in case of an error
        if os.path.exists(audio_file_path):
            os.remove(audio_file_path)
        return None

def get_menu_from_server():
    """
    Fetches the menu data from our MCP server.
    """
    server_url = "http://127.0.0.1:8000/menu"
    try:
        response = requests.get(server_url)
        # Raise an exception if the request failed
        response.raise_for_status()
        # Return the JSON data from the response
        return response.json().get("menu", [])
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to MCP server: {e}")
        return None


if __name__ == "__main__":
    # This block runs when the script is executed directly
    
    # 1. Get API keys
    gemini_key, sarvam_key = get_api_keys()
    
    # 2. Listen for Telugu speech from the microphone
    temp_audio_file = listen_for_telugu_speech()
    
    # 3. Transcribe the speech to text
    transcribed_text = transcribe_telugu_speech(temp_audio_file, sarvam_key)
    
    if transcribed_text:
        print(f"Transcribed (Telugu): {transcribed_text}")

    # Query Gemini with the transcribed text
    gemini_response = query_gemini(transcribed_text)
    print(f"Gemini response: {gemini_response}")

    # 4. (New Logic) If user asks for menu, get it from the server
    if "మెనూ" in transcribed_text:
        menu_items = get_menu_from_server()
        if menu_items:
            print("\n--- Menu Items from MCP Server ---")
            for item in menu_items:
                print(f"- {item['name']}: ₹{item['price']:.2f}")
            print("------------------------------------")
