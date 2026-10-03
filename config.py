import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WA_TOKEN = os.getenv("WA_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

for name in ["GROQ_API_KEY", "WA_TOKEN", "PHONE_NUMBER_ID", "VERIFY_TOKEN"]:
    if not globals()[name]:
        raise ValueError(f"Missing {name} in .env file")