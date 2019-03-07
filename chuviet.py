import cv2;
import matplotlib.pyplot as plt;
import numpy as np;

img =cv2.imread('D:/python/test_images/digits.png')
img_nhandang =cv2.imread('D:/python/anhso.jpg')
#cat hinh theo chieu horizaltal
cells = [np.hsplit(row,100) for  row in np.vsplit(img,50)];


#convert ve kieu array numpy
array   =   np.array(cells);
array_nhandang= np.array(img_nhandang)
#tạo dữ liệu train và test
train  =array[:,:50].reshape(-1,400).astype(np.float32);
##test   =array[:,50:100].reshape(-1,400).astype(np.float32);

test2   =array_nhandang.reshape(-1,400).astype(np.float32);
# gán nhãn cho dữ liệu train
k   =np.arange(10);

#lap lai 250 lan 
train_labels    =np.repeat(k,250)[:,np.newaxis]

#nhận dạng
knn = cv2.ml.KNearest_create();
knn.train(train , train_labels);

#tim 3 so gan nhat
kq1,kq2,kq3,kq4  = knn.findNearest(test2,3)
print(kq1)




# cv2.waitKey(0);
# cv2.destroyAllWindows();