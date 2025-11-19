import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def get_model(model_name="gemini-pro-latest"):
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "Missing API key. Please set GOOGLE_API_KEY in your environment or .env file."
        )

    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 1.0,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
    )

    return model