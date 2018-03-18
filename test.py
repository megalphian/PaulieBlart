import json
from watson_developer_cloud import VisualRecognitionV3

fileName = 'test.jpg'
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

with open(fileName, 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters=json.dumps({
            'classifier_ids': ['peopleRecognition_1276924708'],
            'threshold': 0
        }))
print(json.dumps(classes, indent=2))