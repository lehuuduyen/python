import cv2;

img= cv2.imread('dave2.jpg',1);
cv2.line(img,(180,180),(360,360),(200,200,200),3);
cv2.imwrite('dave3.jpg',img);

cv2.imshow('imgae',img);
cv2.waitKey();
cv2.destroyAllWindows();