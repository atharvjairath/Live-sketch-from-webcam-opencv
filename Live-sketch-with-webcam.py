import cv2
import numpy as np
import os


# A function which converts a image to sketch
def sketch(white,image):

    #converts the image into grayscale
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # Lets clean this image
    img_blur = cv2.GaussianBlur(img_gray,(5,5),0)

    #to give it a sketch feel we need to extract the edges
    img_canny = cv2.Canny(img_blur,0,40)
    final_image = img_canny

    if white == 1:
        #now to turn it to white 
        ret,img_white = cv2.threshold(img_canny,70,255,cv2.THRESH_BINARY_INV)
        final_image = img_white

    frame = cv2.flip(final_image,1)
    return frame




#Open webcam
camera = cv2.VideoCapture(0)

img_counter = 0

# Menu
print("Welcome to Live Sketch with webcam! Choose your settings")
print("1. White ")
print("2. Black ")
print("Enter your Option 1 or 2 ")
canvas = int(input())

#loop to read images and show them

while True:
    ret, frame = camera.read()
    frame = sketch(canvas,frame)
    cv2.imshow("Your Sketch Window!",frame)
    if cv2.waitKey(1) == 13:
        break

    #to save frames in a folder
    elif cv2.waitKey(1)%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        
        #add your own path here
        path = "C:/Users/Atharv/Desktop/ismein sara kaam hai mera/Open-Cv_Practice/Images"

        #making directory only first time!
        if img_counter == 0:
            os.mkdir(path)
    
        cv2.imwrite(os.path.join(path,img_name), frame)
        print("{} written!".format(img_name))
        img_counter += 1


camera.release()
cv2.destroyAllWindows()





