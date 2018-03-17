import cv2
import imgurpython

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()
cv2.imwrite('img.png', frame)

client = imgurpython.ImgurClient(client_id, client_secret)
client.set_user_auth(access_token, refresh_token)
url = client.upload_from_path('img.png', anon=False)['link']
print(url)
