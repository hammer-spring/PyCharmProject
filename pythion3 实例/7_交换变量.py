'''
通过用户输入两个变量，并相互交换：
'''
'''
#用户输入
x = input('输入x值：')
y = input('输入y值：')

#创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后x的值为:{}'.format(x))
print('交换后y的值为:{}'.format(y))
'''
#不使用临时变量
#x,y = y,x
# 用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 不使用临时变量
x, y = y, x

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))