from flask import Flask, request
import config
import whatsapp

app = Flask(__name__)

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
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

    whatsapp.send_message(sender, f"You said: {text}")
    return "ok", 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)