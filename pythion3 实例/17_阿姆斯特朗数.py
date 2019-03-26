'''
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
'''
# 获取用户输入数字
lower = int(input("最小值: "))
upper = int(input("最大值: "))

for num in range(lower, upper + 1):
    # 初始化 sum
    sum = 0
    # 指数
    n = len(str(num))

    # 检测
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if num == sum:
        print(num)