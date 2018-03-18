import json
import imgurpython
import twilio.rest
import serial
from watson_developer_cloud import VisualRecognitionV3


fileName = 'test.jpg'
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='09e2221c5a344fb0765f38c795bbdf425e96a088')# 'fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

# classify image
with open(fileName, 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters=json.dumps({
            'classifier_ids': ['peopleRecognition_813562303'], # ['peopleRecognition_1276924708'],
            'threshold': 0
        }))

results = { row['class'] : row['score'] for row in classes['images'][0]['classifiers'][0]['classes'] }

if results:
    highest = max(results.items(), key=lambda class_score: class_score[1])[0]

    if results[highest] > 0.5:
        # upload to imgur
        imgur_client = imgurpython.ImgurClient(env('IMGUR_CLIENT_ID'), env('IMGUR_CLIENT_SECRET'))
        imgur_client.set_user_auth(env('IMGUR_ACCESS_TOKEN'), env('IMGUR_REFRESH_TOKEN'))
        imgur_url = imgur_client.upload_from_path('img.bmp', anon=False)['link']
        print(imgur_url)

        # send text message through twilio
        res = twilio.rest.Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN')).messages.create(
                to = '+16098656527',
                body = 'INTRUDER DETECTED: ' + highest,
                from_ = '+17324106248',
                media_url = imgur_url,
            )
        print(res)
