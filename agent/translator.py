from langdetect import detect
import openai
from agent.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def translate_to_english(text):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Translate this to English: {text}"}]
    )
    return response.choices[0].message["content"]

def translate_back(text, target_lang):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Translate this to {target_lang}: {text}"}]
    )
    return response.choices[0].message["content"]
