from yolo import YOLO, detect_video
from PIL import Image
import cv2
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    yolo=YOLO()
    while 1:
        ret, img = cap.read()
        # img = cv2.imread("./0.jpg")
        cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
        pilimg = Image.fromarray(cv2img)
        r_image = yolo.detect_image(pilimg)
        # r_image.show()
        cv2charimg = cv2.cvtColor(np.array(r_image), cv2.COLOR_RGB2BGR)
        cv2.imshow('img', cv2charimg)
        k = cv2.waitKey(30) & 0xff

    yolo.close_session()

