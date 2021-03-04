print ("-----------")
print ('成绩单分类|' )
print ("-----------")
temp = input ("输入分数值：")
A = int (temp)
if 100 >= A >= 90:
    print ("=成绩是A")
if 80 <= A < 90:
    print ("成绩是B")
if 60 <= A < 80:
    print ("成绩是C")
if 0 <= A < 60 :
    print ("成绩是D")
if 100 < A or A < 0  :
    print ("错误输入值！请输入0到100之间的数值")