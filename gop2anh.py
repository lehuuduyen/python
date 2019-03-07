import cv2; 


imgg	= cv2.imread('gril.jpg',1);


imgp	= cv2.imread('phongcanh.jpg',1);
print(imgp.shape)

imgg	= imgg[0:320,0:240];

imgp	= imgp[0:320,0:240];

img3 	= cv2.add(imgg,imgp);


cv2.imshow('image',img3);


cv2.waitKey();