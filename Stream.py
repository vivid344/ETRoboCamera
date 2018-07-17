import cv2

URL = "http://192.168.11.100:8080/?action=streamå"
stream_video = cv2.VideoCapture(URL)

while True:
    ret, img = stream_video.read()
    cv2.imshow("Stream Video", img)
    key = cv2.waitKey(1) & 0xff  # 64bitマシーンを使っている場合は "&" 以降の処理が必要
    if key == ord("q"):
        break
