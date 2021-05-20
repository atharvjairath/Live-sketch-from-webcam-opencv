import cv2
import numpy as np


# A function which converts a image to sketch
def sketch(image):

    #converts the image into grayscale
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Lets clean this image
    img_blur = cv2.GaussianBlur(img_gray,(5,5),0)


    return img_blur




#Open webcam

camera = cv2.VideoCapture(0)


#loop to read images and show them

while True:
    ret, frame = camera.read()
    cv2.imshow("Your Sketch Window!", sketch(frame))
    if cv2.waitKey(1) == 13:
        break


camera.release()
cv2.destroyAllWindows()





