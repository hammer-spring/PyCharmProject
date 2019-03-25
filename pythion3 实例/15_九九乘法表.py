'''
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
#通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。
'''
#一句话输出！
print('\n'.join(' '.join("%dx%d=%-2d" % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)))