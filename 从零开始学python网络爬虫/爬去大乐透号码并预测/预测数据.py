
import numpy as np
import pandas as pd
import os

data = pd.read_csv(r"D:\PyCharm\PyCharmProject\从零开始学python网络爬虫\爬去大乐透号码并预测\simple_data.csv", sep=' ', header=None)
data = data.sort_index(ascending=False).values  # 数据反过来
data = data[:, 1:]


def fengbu(i):
    abb = {}
    for l in range(7):
        for n in range(1, 36):
            abb[l, n] = []
            for qiu in range(i - 1):
                if data[qiu][l] == n:
                    a = data[qiu + 1][l] - data[qiu][l]
                    abb[l, n].append(a)  # 一个大字典为{（l,n):a}
    dict1 = {}
    dict2 = {}  # 每个数字增大的概率
    add1 = {}  # 增大的次数
    reduce = {}  # 减小的次数
    da = {}
    jian = {}
    da1 = []
    jian1 = []
    dict21 = []
    for n, l in abb.items():
        add1[n] = 0
        reduce[n] = 0
        da[n] = 0
        jian[n] = 0
        for m in l:
            if m > 0:
                add1[n] += 1  # 统计往期为这个数字时下次增大次数
            elif m < 0:
                reduce[n] += 1  # 减小次数

        dict2[n] = round(add1[n] / (reduce[n] + add1[n] + 1), 4)
        # 得到前面那张概率图 减小和它相反
        for m in set(l):
            if m > 0:
                dict1[n, m] = (round(l.count(m) / add1[n], 4)) * m
                da[n] += dict1[n, m]
                '''
                这是基于首先判断当前期每个数字增大或减小概率哪个大
                数值大的进一步细化，即将具体增大或减小的值得概率当
                成权重再分别与之对应值相乘,在全部相加为下一次预测值

                '''
            elif m < 0:
                dict1[n, m] = (round(l.count(m) / reduce[n], 4)) * m
                jian[n] += dict1[n, m]
            elif m == 0:
                dict1[n, m] = 0  # 两次数字不变
    for n, m, l in zip(da.values(), jian.values(), dict2.values()):
        da1.append(n)  # 原来是字典现在要将其弄成矩阵
        jian1.append(m)
        dict21.append(l)
    da1 = np.array(da1).reshape(7, 35)
    jian1 = np.array(jian1).reshape(7, 35)
    dict21 = np.array(dict21).reshape(7, 35)
    # shuan
    return da1, jian1, dict21


def predict(i):
    for red in range(7):
        print(round(data[:, red].mean(), 4), round(data[:, red].std(), 4))
        #当前均值
        #方差
    da1, jian1, dict21 = fengbu(i)
    predict = np.zeros(7)
    for l in range(7):
        for m in range(1, 34):
            if data[i][l] == m:
                if dict21[l][m - 1] > 0.5:
                    print(dict21[l][m - 1], da1[l][m - 1], data[i][l])
                    # 每期每个数字增大或减小概率，权重和，每个数字值
                    predict[l] = data[i][l] + da1[l][m - 1]
                elif dict21[l][m - 1] < 0.5:
                    print(dict21[l][m - 1], jian1[l][m - 1], data[i][l])
                    predict[l] = data[i][l] + jian1[l][m - 1]
    print("第 %d 次,结果是:%s" % (i, data[i]))
    print("所以预测下一次是:%s" % predict)
    print("真正下一次是:%s" % data[i + 1])
    print('*' * 50)


if __name__ == '__main__':
    predict(1641)