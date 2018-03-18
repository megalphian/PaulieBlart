from watson_developer_cloud import VisualRecognitionV3
import serial
import random
import time
import json
import imgurpython
import twilio.rest
import os, sys

env = os.environ
imgur_client = imgurpython.ImgurClient(env['IMGUR_CLIENT_ID'], env['IMGUR_CLIENT_SECRET'])
imgur_client.set_user_auth(env['IMGUR_ACCESS_TOKEN'], env['IMGUR_REFRESH_TOKEN'])
twilio_client = twilio.rest.Client(env['TWILIO_ACCOUNT_SID'], env['TWILIO_AUTH_TOKEN'])
s = serial.Serial('/dev/ttyUSB0', 9600)
send = lambda x: s.write(str(x).encode())

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='143b3817d38a28bfef4e3b1e8eb5b7ead9a56b3b') # 'fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')


def call_watson():
    # classify image
    with open('image.jpg', 'rb') as images_file:
        response = visual_recognition.classify(
            images_file,
            parameters=json.dumps({
                'classifier_ids': ["peopleRecognition_1329776309"],
                'threshold': 0
            }))

    results = { row['class'] : row['score'] for row in response['images'][0]['classifiers'][0]['classes'] }
    print(results)

    if results:
        highest = max(results.items(), key=lambda class_score: class_score[1])[0]

        if results[highest] >= 0.5:
            # upload to imgur
            imgur_url = imgur_client.upload_from_path('image.jpg', anon=False)['link']
            print(imgur_url)

            # send text message through twilio
            res = twilio_client.messages.create(
                    to = '+15875895810',
                    body = 'INTRUDER DETECTED: ' + highest,
                    #from_ = '+17324106248',
                    from_ = '+19029185551',
                    media_url = imgur_url,
                )
            print(res)


def start_run():
    print("starting")
    while True:
        try:
            direction = random.choice([1, 5])
            for _ in range(4):
                send(direction)
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


if __name__ == '__main__':
    start_run()
