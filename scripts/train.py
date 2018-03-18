import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

print('before slow json upload')

with open('frank.zip', 'rb') as frank,\
    open('dan.zip', 'rb') as dan:
    #open('brian.zip', 'rb') as brian,\
    #open('megatron.zip', 'rb') as megatron,\
    #open('empty.zip', 'rb') as emptySpace:
    model = visual_recognition.create_classifier(
        'peopleRecognition',
        frank_positive_examples=frank,
        dan_positive_examples=dan)
        #brian_positive_example=brian,
        #megatron_positive_example=megatron,
       # negative_examples=emptySpace)

with open('results.txt', 'w') as outfile:
    json.dump(model, outfile, indent=2)