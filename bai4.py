import cv2;


img	= cv2.imread('dave4.png',1);

#cao tu tren xuong , chieu rong tu trái qua 
cut	= img[300:800,100:600];


cv2.imshow('image',cut)
cv2.waitKey();


#chieu cao, rong , ma mau 
print(img.shape)
#kich thuoc
print(img.size /1000)

# kieu 8byte
print(img.dtype)
