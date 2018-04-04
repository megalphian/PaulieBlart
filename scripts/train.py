import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

print('before slow json upload')

with open('frank.zip', 'rb') as frank,\
    open('dan.zip', 'rb') as dan:
    model = visual_recognition.create_classifier(
        'peopleRecognition',
        frank_positive_examples=frank,
        dan_positive_examples=dan)

with open('results.txt', 'w') as outfile:
    json.dump(model, outfile, indent=2)