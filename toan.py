# -*- coding: utf-8 -*-
import heapq
from collections import Counter
grades =[12,32,5,8,88,1544,788,7952,2558,362,4485]

print(heapq.nlargest(len(grades),grades))



stocks =[
{
	"name": "duyen" , "age":10	
},
{
	"name": "my"	, "age":29
},
{
	"name": "long"	, "age":19
},
{
	"name": "my3"	, "age":39
},
{
	"name": "my2"	, "age":9
},
{
	"name": "my1"	, "age":129
}
]


print(heapq.nsmallest(4,stocks,key=lambda stock:stock['age']))


stocks ={
	"age1":10,
	"age2":29,
	"age3":19,
	"age4":39,
	"age5":9,
	"age6":129
}







print(list(zip(stocks.values(),stocks.keys())))



# dem so phan tu
string='Đây là khái niệm khá phổ biến của người làm SEO. 1 bài viết tốt để lên top Google ngoài yếu tố hữu ích cần tuân theo các quy tắc kỹ thuật nhằm giúp Google nhanh chóng nhận diện ra nội dung và đưa tới người tìm kiếm. Viết bài chuẩn SEO gồm các nguyên tắc về mật độ từ khoá, sử dụng định dạng văn bản phù hợp và các tính toán chi tiết nhằm tối ưu nhất cho cụm từ (các cụm từ khoá) mục tiêu. Google ngày càng khó tính với các “thủ thuật SEO quá đà”, đặc biệt là tạo backlink không tự nhiên sau khi Google update Penguin hoạt động realtime. Điều này là tin buồn với giới SEO vốn chú trọng vào phương pháp backlink, nhưng lại là tin vui vào những ai theo trường phái SEO tổng thể tập trung vào nội dung. Nếu ví von việc Thiết kế ra một website chuẩn SEO (bao gồm Cấu trúc website và tối ưu kỹ thuật cho Website – Onpage) là nền móng thì Content SEO chính là “da thịt”. Làm sao để viết ra một nội dung vừa hay ho, vừa chuẩn các yếu tố để SEO, giữ chân được người dùng và tăng tương tác mạng xã hội là điều chắc chắn sẽ được toàn thể giới SEO hiện nay quan tâm (khi mà backlink trở nên khó khăn). SEONGON xin giới thiệu 35 checklist công việc để bạn tạo ra một nội dung chuẩn SEO. Tài liệu dựa trên kinh nghiệm và kiến thức SEO của SEONGON và tham khảo các tư liệu từ những Guru trong ngành công nghiệp SEO của thế giới.'

arr_str=string.split()

counter= Counter(arr_str);

top_three= counter.most_common(3)
print(top_three)
#[('SEO', 9), ('là', 7), ('các', 6)]
