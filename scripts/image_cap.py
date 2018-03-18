import pygame
import pygame.camera
from pygame.locals import *
from PIL import Image

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0")
cam.start()
image = cam.get_image()

pil_string_image = pygame.image.tostring(img,"RGBA",False)
im = Image.frombytes("RGBA",(0,),pil_string_image)
im.save('test.jpg')

