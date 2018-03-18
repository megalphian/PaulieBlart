import cv2
import json
import pygame
import pygame.camera

def capture():
    pygame.camera.init()
    cam_list = pygame.camera.list_cameras()
    camera = pygame.camera.Camera(cam_list[0], (640, 480))
    camera.start()
    return camera.get_image()

# Image Float Float -> Image
def slice(img, start, end):
    width, height = img.get_size()
    sub_start = int(width * start)
    sub_width = int(width * end) - sub_start
    return img.subsurface( (sub_start, 0, sub_width, height) )

# Image -> Bool
def alarm(img):
    pass # query watson

# Image -> Int
def direction(img):
    if not alarm(img): return -1
    elif alarm(slice(img, 0, 0.25)): return 1
    elif alarm(slice(img, 0, 0.50)): return 2
    elif alarm(slice(img, 0.75, 1)): return 5
    elif alarm(slice(img, 0.50, 1)): return 4
    else:
        return 3

if __name__ == '__main__':
    # print(direction(capture()))
    img = pygame.image.load('img.png')
    pygame.image.save(slice(img, 0, 0.5), 'img1.png')
    pygame.image.save(slice(img, 0.5, 1), 'img2.png')
    pygame.image.save(slice(img, 0.3, 0.7), 'img3.png')

