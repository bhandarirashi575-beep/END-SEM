from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("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"))

def call_llm(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",   # ✅ UPDATED MODEL
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"