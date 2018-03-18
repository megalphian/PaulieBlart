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
            subprocess.call(['python3', 'control_bot.py'])
            resp.message("Starting Patrol")
        elif body == 'no':
            # subprocess.call(['pkill', '-f', 'control_bot.py'])
            os.system("kill $(ps aux | grep '[p]ython control_bot.py' | awk '{print $2}')")
            resp.message("Stopping Patrol")
        return str(resp)

    except:
        resp.message("Invalid")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
