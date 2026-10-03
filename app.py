from flask import Flask, request
import config
import whatsapp
import llm

app = Flask(__name__)

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    print(mode)
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print("Received token:", repr(token))
    print("Expected token:", repr(config.VERIFY_TOKEN))

    if mode == 'subscribe' and token == config.VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def receive():
    data = request.get_json()

    msg = whatsapp.parse_message(data)
    if msg is None:
        return 'ok', 200

    sender, text = msg
    print(f"From {sender}: {text}")

    reply = llm.get_reply(text)
    whatsapp.send_message(sender, reply)
    
    return "ok", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)