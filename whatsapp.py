import requests
import config

def parse_message(data):
    try:
        value = data['entry'][0]['changes'][0]['value']
        msg = value['messages'][0]
    except (KeyError, IndexError):
        return None

    if msg.get('type') != 'text':
        return None

    return msg['from'], msg['text']['body']


def send_message(to, text):
    url = f"https://graph.facebook.com/v21.0/{config.PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {config.WA_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text},
    }

    r = requests.post(url, headers=headers, json=payload, timeout=10)
    print("Send status:", r.status_code, r.text)
    return r.status_code == 200