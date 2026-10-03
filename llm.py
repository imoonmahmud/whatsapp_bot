from groq import Groq
import config

client = Groq(api_key=config.GROQ_API_KEY)

SYSTEM_PROMPT = (
    "You are a helpful assistant on WhatsApp. "
    "Reply short and clear. Reply in the same language the user writes "
    "(Bengali or English)."
)

def get_reply(user_text, history=None):
    history = history or []
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {'role': 'system', 'content': SYSTEM_PROMPT},
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