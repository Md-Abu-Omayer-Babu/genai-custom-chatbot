import os
import google.generativeai as genai

api_key = os.environ.get("your_api_key")
genai.configure(api_key = api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

chat_session = model.start_chat()

while True:
    print("You: ", end="")
    topic = input()
    user_prompt = f"What's the Islamic perspective on {topic}?\
        Please provide references from the Quran and authentic Hadith books such as Sahih al-Bukhari, Sahih Muslim, Sunan Abu Dawood, Jami al-Tirmidhi, Sunan al-Nasa'i, and Sunan Ibn Majah.\
        give the short answer!\n"

    chat_session.history.append({
        "role": "user",
        "parts": [user_prompt]
    })

    response = chat_session.send_message(user_prompt)

    chat_session.history.append({
        "role": "model",
        "parts": [response.text]
    })

    print(response.text)
