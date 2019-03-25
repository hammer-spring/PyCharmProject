'''
# 输出指定范围内的素数

# take input from the user
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
'''
import math
# 输出指定范围内的素数
# 用户输入范围
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
print("素数结果如下：")
print("="*10)
pri_num = 0
com_num = 0
for num in range(lower, upper + 1):
    # 找到其平方根（ √ ），减少算法时间
    square_num = math.floor(num ** 0.5)
    # 素数大于 1
    if num > 1:
        for i in range(2, (square_num + 1)):
            if (num % i) == 0:
                com_num += 1
                break
        else:
            pri_num += 1
            print(num)
print("="*10)
print(com_num,'个合数')
print(pri_num,'个素数')