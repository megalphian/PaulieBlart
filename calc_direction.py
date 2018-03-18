import json
import pygame
import pygame.camera
import watson_developer_cloud
# import cv2

visual_recognition = watson_developer_cloud.VisualRecognitionV3('2016-05-20',
                        api_key='fdbed6c3c7053723edbcdbc1259bc96e97b14c4e')

def capture():
    pygame.camera.init()
    cam_list = pygame.camera.list_cameras()
    camera = pygame.camera.Camera(cam_list[0], (640, 480))
    camera.start()
    return camera.get_image()
    # cap = cv2.VideoCapture(0)
    # ret, frame = cap.read()
    # cap.release()
    # return frame

def slice(img, start, end):
    width, height = img.get_size()
    sub_start = int(width * start)
    sub_width = int(width * end) - sub_start
    img = img.subsurface( (sub_start, 0, sub_width, height) )
    filename = 'img_{}_{}'.format(start, end).replace('.', '-') + '.png'
    pygame.image.save(img, filename)
    return filename

def alarm(filename):
    with open(filename, 'rb') as img_file:
        result = visual_recognition.classify(
            img_file,
            parameters = '''{
                "classifier_ids" : ["peopleRecognition_1276924708"],
                "threshold" : 0.0
            }'''
        )

    scores = ( row['score'] for row in result['images'][0]['classifiers'][0]['classes'] )
    print(result['images'][0]['classifiers'][0]['classes'])
    return max(scores) > 0.5

# Image -> Int
def direction(img, filename):
    if not alarm(filename): return -1
    elif alarm(slice(img, 0, 0.25)): return 1
    elif alarm(slice(img, 0, 0.50)): return 2
    elif alarm(slice(img, 0.75, 1)): return 5
    elif alarm(slice(img, 0.50, 1)): return 4
    else:
        return 3

if __name__ == '__main__':
    pic = capture()
    # cv2.imwrite('img.png', pic)
    # img = pygame.image.load('img.png')
    # print(direction(img, 'img.png'))

    # right = slice(img, 0, 0.5)
    # left  = slice(img, 0.5, 1)
    # mid   = slice(img, 0.25, 0.75)

    # alarm(left)
    # alarm(mid)
    # alarm(right)
