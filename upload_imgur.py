import pygame.camera
import imgurpython
import twilio.rest
import os

env = lambda s: os.environ[s]

# get capture from video feed
pygame.camera.init()
cam_list = pygame.camera.list_cameras()
camera = pygame.camera.Camera(cam_list[0], (640, 480))
camera.start()
pygame.image.save(camera.get_image(), 'img.png')

# upload to imgur
imgur_client = imgurpython.ImgurClient(env('IMGUR_CLIENT_ID'), env('IMGUR_CLIENT_SECRET'))
imgur_client.set_user_auth(env('IMGUR_ACCESS_TOKEN'), env('IMGUR_REFRESH_TOKEN'))
imgur_url = imgur_client.upload_from_path('img.png', anon=False)['link']
print(imgur_url)

# send image via text message
res = twilio.rest.Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN')).messages.create(
        to = '+16098656527',
        body = 'some shits goin down yo',
        from_ = '+17324106248',
        media_url = imgur_url,
    )
print(res)
