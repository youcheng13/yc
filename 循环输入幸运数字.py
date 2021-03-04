import random

a = random.randint(0,9)
b = int(input ("请输入漂亮数字："))
c = 1

while True:
    if b == a:
        break
    b = int(input("请重新输入你的数字："))
    c += 1
    # print(b)
    print(c)

print("太帅了！! ! \n"+"你是第 %d 个输入的  洗 碗 * 幸 运 之 星 ！！!"%c)
print('去洗碗吧！')
print('去洗碗吧！')
print('去洗碗吧！')
print('去洗碗吧！')
print('去洗碗吧！')





