from PIL import Image

img 	= Image.open("test_images/test.jpg");
##### chuyen đổi khung màu
r,g,b	= img.split();
newimg	= Image.merge("RGB",(r,g,b))

##### resize and lật ngược ảnh
img_resize=img.resize((300,200));
img_transpose=img.transpose(Image.FLIP_LEFT_RIGHT)
img_rotate=img.transpose(Image.ROTATE_180)

img_rotate.show()



##### cắt hình
# x, y, x + width , y + height
area	= (200,100,350,575)

img_crop= img.crop(area)
# crop_img.save('anh.jpg')



imcome = [10,30,75];
def double(dolar):
	return dolar *2;

print(list(map(double,imcome)))