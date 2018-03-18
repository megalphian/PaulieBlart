# Imports needed for the API call/Image Capture
import json
from watson_developer_cloud import VisualRecognitionV3
import cv2

# Number of images captured
imageNumber = 0
# Name of the file that will be saved
picName = ''
# Initializing the Watson Visual Recognition API
visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

##########  identifyTargets  #######################################
# Use:  Takes picture from camera on mobile platform.
#       Then sends it to the Watson API.
#       The returned JSON file is then saved to later be parsed.
###################################################################
def identifyTargets():
    # Accessing the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    # Saving the file
    picName = 'test' + str(imageNumber) + '.png'
    cv2.imwrite(picName, frame)

    # Posting to the Watson API
    with open(picName, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file,
            parameters=json.dumps({
                'classifier_ids': ['peopleRecognition_1276924708'],
                'threshold': 0
        }))

        # Save it to text file for later parsing
        fileName = 'json' + str(imageNumber) + '.txt'
        with open(fileName, 'w') as outfile:
            json.dump(classes, outfile, indent=2)

identifyTargets()