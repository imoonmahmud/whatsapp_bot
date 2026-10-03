from groq import Groq
import config
from prompts import get_prompt

client = Groq(api_key=config.GROQ_API_KEY)

def get_reply(user_text, history=None):
    history = history or []
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {'role': 'system', 'content': get_prompt()},
                *history,
                {'role': 'user', 'content': user_text}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Groq error:", e)
        return "Something went wrong"