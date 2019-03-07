import cv2;

img	=	cv2.imread('digits.jpg',1);

for i in range(180,340):
	print(i);
	img[i][i]=[83,212,0];
cv2.imwrite('dave4.png',img)

cv2.imshow('image',img);
cv2.waitKey();
cv2.destroyAllWindows();

