# Modified by Brian Cho
# Last Modified As: 03/17/2018 1:19
# send_sms.py file is to send message from twilio account
from twilio.rest import Client

# Unique Number under account
account_sid = "AC80f6c0e127a3d4e2f190077fea35962e"
auth_token = "132b3f52264249aecb49bb2efd093786"

# Client Setup: Message to, Message from, and the body
client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+17143357534",
    from_="+19097570441",
    body="Hello there!")
