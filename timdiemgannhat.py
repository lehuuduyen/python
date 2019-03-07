import cv2;
import numpy as np;
import matplotlib.pyplot as plt;

trainData	= np.random.randint(0,100,(25,2)).astype(np.float32);
ketqua		= np.random.randint(0,2,(25,1)).astype(np.float32);	
new			= np.random.randint(0,100,(1,2)).astype(np.float32);

red			= trainData[ketqua.ravel()==1]
blue		= trainData[ketqua.ravel()==0]

#x ,y , do lon , mau , hinh
plt.scatter(red[:,0],red[:,1],100,'r','s')
plt.scatter(blue[:,0],blue[:,1],100,'b','^')
plt.scatter(new[:,0],new[:,1],100,'g','>')


knn	=cv2.ml.KNearest_create();
knn.train(trainData,0,ketqua);
name="le huu duyen"
#tim new 3 ng gan nhat
temp,ketqua,hangxom,khoangcach	= knn.findNearest(new,3)
ketqua=ketqua[0][0].astype(np.int);
if ketqua==1:mau="Result: red"
else: mau="Result: blue"



print("hangxom:{}".format(hangxom));
print("khoangcach:{}".format(khoangcach));
print("temp:{}".format(temp));
print("ketqua:{} va nhu vay do {}".format(mau,name));
print("{} ".format(mau));
plt.savefig('ketqua.png')


#plt.show();





