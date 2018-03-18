import twilio.rest
import subprocess
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    print('Here')
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()
    try:
        # Determine the right reply for this message
        if body == 'go':
            subprocess.check_output(['python', 'control_bot.py'])
            resp.message("Starting Patrol")
        elif body == 'no':
            output = subprocess.check_output(['pkill', '-f', 'control_bot.py'])
            resp.message("Stopping Patrol. Output: %s" % output)
        return str(resp)

    except:
        resp.message("Invalid")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
