import random;
import urllib.request;


def dowloadimage(url):
	name	=	random.randrange(1,100);
	fullname=	str(name)+".jpg";
	urllib.request.urlretrieve(url,fullname);


dowloadimage('https://www.w3schools.com/w3css/img_lights.jpg');