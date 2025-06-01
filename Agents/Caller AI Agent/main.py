from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello! Your Flask app is running."

@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello! This is your AI voice assistant.")
    response.pause(length=1)
    response.say("How can I help you today? ")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
