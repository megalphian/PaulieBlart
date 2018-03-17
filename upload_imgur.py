import cv2
import imgurpython
import twilio.rest
import os

env = lambda s: os.environ[s]

# get capture from video feed
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()
cv2.imwrite('img.png', frame)

# upload to imgur
imgur_client = imgurpython.ImgurClient(env('IMGUR_CLIENT_ID'), env('IMGUR_CLIENT_SECRET'))
imgur_client.set_user_auth(env('IMGUR_ACCESS_TOKEN'), env('IMGUR_REFRESH_TOKEN'))
imgur_url = imgur_client.upload_from_path('img.png', anon=False)['link']
print(imgur_url)

# send image via text message
res = twilio.rest.Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN')).messages.create(
        to = '+16098656527',
        body = 'some shits goin down yo',
        from_ = '+17324106248',
        media_url = imgur_url,
    )
print(res)
