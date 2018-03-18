# Modified by Brian Cho
# Last Modified As: 03/17/2018 7:35
# run.py file is to create local port to run to get a message from other to twilio account.
# required library installed: flask, twilio, pip, virtualenv
# required setup: ngrok (command: ./ngrok <port#>)
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['POST'])

def sms_reply():
    data = request.values["Body"]
    print(data)

    resp = MessagingResponse()
    resp.message("Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)