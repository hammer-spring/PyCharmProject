import numpy as np
def img2vector(filename):
    # 创建向量
    returnVect = np.zeros((1, 1024))
    # 打开数据文件，读取每行内容
    fr = open(filename)
    for i in range(32):
        # 读取每一行
        lineStr = fr.readline()
        # 将每行前 32 字符转成 int 存入向量
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])

    return returnVect

print(img2vector('digits/testDigits/0_1.txt'))
