import urllib.request;
import random;



file_garena='https://docs.google.com/spreadsheets/d/1Nk-nFm34WZffVyv0LRvgxAl68QkF9l8rMEPAmAHXGRs/edit?usp=sharing'



def dowloadfile(url):
	response	= urllib.request.urlopen(url);
	csv			= response.read();
	csv_str		= str(csv);
	lines		=csv_str.split("\\n");
	dest_url	= r'goog.csv'
	fx			= open(dest_url,'w');
	for line in lines:
		fx.write(line +"\n")
	fx.close();	


dowloadfile(file_garena)	