import json
import os
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-04-04',
    api_key='8ba18ee276c2d712803ab3ef658403c965bf12ce')

data_dir = "../Dataset"

with open(os.path.join(data_dir, "Megnath.zip"), 'rb') as meg,\
    open(os.path.join(data_dir, "negative.zip"), 'rb') as negative:
    model = visual_recognition.create_classifier(
        'peopleRecognition',
        megnath_positive_examples=meg,
        negative_examples=negative)

with open('results.txt', 'w') as outfile:
    json.dump(model, outfile, indent=2)