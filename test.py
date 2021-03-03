
#!/usr/bin/env python3
#-*- coding:utf-8 -*-


ma_dic = {'jiangqi':'ma'}
with open('1.txt','w') as f:
    print(ma_dic)
    print(type(ma_dic))
    dd = str(ma_dic)
    print(type(dd))
    f.write(dd)

