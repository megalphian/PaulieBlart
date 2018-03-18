import os, sys

import json
import imgurpython
import twilio.rest
import serial
import random
import time
import subprocess
from watson_developer_cloud import VisualRecognitionV3

fileName = 'image.jpg'
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='fdbed6c3c7053723edbcdbc1259bc96e97b14c4e') # 'fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

env = os.environ

def call_watson():
    # classify image
    with open(fileName, 'rb') as images_file:
        response = visual_recognition.classify(
            images_file,
            parameters=json.dumps({
                'classifier_ids': ["peopleRecognition_751539008"],
                'threshold': 0
            }))

    results = { row['class'] : row['score'] for row in response['images'][0]['classifiers'][0]['classes'] }
    print(results)

    if results:
        highest = max(results.items(), key=lambda class_score: class_score[1])[0]

        if results[highest] >= 0.5:
            # upload to imgur
            imgur_client = imgurpython.ImgurClient(env['IMGUR_CLIENT_ID'], env['IMGUR_CLIENT_SECRET'])
            imgur_client.set_user_auth(env['IMGUR_ACCESS_TOKEN'], env['IMGUR_REFRESH_TOKEN'])
            imgur_url = imgur_client.upload_from_path('image.jpg', anon=False)['link']
            print(imgur_url)

            # send text message through twilio
            res = twilio.rest.Client(env['TWILIO_ACCOUNT_SID'], env['TWILIO_AUTH_TOKEN']).messages.create(
                    to = '+15875895810',
                    body = 'INTRUDER DETECTED: ' + highest,
                    #from_ = '+17324106248',
                    from_ = '+19029185551',
                    media_url = imgur_url,
                )
            print(res)

if __name__ == "__main__":
    s = serial.Serial('/dev/ttyUSB0', 9600)
    send = lambda x: s.write(str(x).encode())

    while True:
        try:
            for _ in range(4):
                send(random.choice([1,5]))
                time.sleep(1)
                send(0)
                os.system('./image_capture.sh')
                call_watson()
            send(random.choice([2, 3, 4]))
            time.sleep(5)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            break

