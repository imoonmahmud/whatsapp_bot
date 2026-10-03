import requests
import config

url = f"https://graph.facebook.com/v21.0/{config.PHONE_NUMBER_ID}"
r = requests.get(url, headers={"Authorization": f"Bearer {config.WA_TOKEN}"})
print(r.status_code, r.text)