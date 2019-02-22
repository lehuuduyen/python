import cv2
import math
import numpy as np

cap =cv2.VideoCapture("abc.mp4")

frameRate =cap.get(5)
x=1
while (cap.isOpened()):
	frameId		=	cap.get(1)
	ret,frame 	=	cap.read()
	if(ret !=True):break
	if(frameId % math.floor(frameRate) ==0):
		filename ="./test_images/image"+ str(int(x)) +".jpg";x+=1
		cv2.imwrite(filename,frame)


cap.release();
print('done')
