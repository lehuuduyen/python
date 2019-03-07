


fw =open('text.txt','wb');
text1=str('nội dung text\n');
fw.write(text1.encode("utf-8"));
fw.write('nội dung text 2'.encode("utf-8"));
fw.close()



fw =open('text.txt','r',encoding='utf-8');
string =fw.read();
print(string)