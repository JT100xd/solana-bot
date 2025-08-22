from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8361735277:AAHidscafkIN6730cj6jalTVEZa2UwkyDRE"
CHAT_ID = "659489181"

def send_alert(msg):
    url = f"https://api.telegram.org/bot{8361735277:AAHidscafkIN6730cj6jalTVEZa2UwkyDRE}/sendMessage"
    requests.post(url, data={"659489181": 659489181, "text": msg})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)  # just for debugging
    send_alert(f"🚨 New transaction: {data}")
    return "ok"

@app.route("/")
def home():
    return "Bot is live!"
