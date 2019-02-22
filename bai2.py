import cv2;
img =cv2.imread('emptybookrec_LargeWide.jpg',1);
#hinh , ve tu toa do , tới tọa độ , mà r g b ,độ rộng 5 px
cv2.line(img,(0,0),(400,300),(255,111,190),5);
#vẽ , lưu ảnh ra
cv2.imwrite('anh1.jpg',img)



#show anh
cv2.imshow('image',img);
#thời gian đợi
cv2.waitKey(0);
#xóa cache
cv2.destroyAllWindows();




print('123');