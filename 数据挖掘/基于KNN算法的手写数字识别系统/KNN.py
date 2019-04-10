'''
KNN算法思想：
K最近邻算法，顾名思义就是搜寻最近的K个已知类别样本用于未知类别样本的预测。
"最近"的度量就是应用点之间的距离或相似性，距离越小或相似度越高，说明他们之间越近
"预测"，对于离散型的因变量来说，从k个最近的已知类别样本中挑选出频率最好的类别用
于未知样本的判断；对于连续性的因变量来说，则是将K个最近的已知样本均值用作未知样
本的预测。

最佳K值的选择
为了在模型中防止出现过拟合或欠拟合状态，也为了获得最佳的k值，可以考虑俩种解决方
案：一种是设置k近邻样本投票权重，假设读者在使用KNN算法进行分类或预测时设置的
k值比较大，担心模型发生欠拟合的现象，一个简单有效的方法就是设置近邻样本的投票权
重，如果一直样本距离未知样本比较远，则对应的权重就设置的低一些，否则权重高一些
通常可以将权重设置为距离的倒数，另一种是采用多重交叉验证，最后选出平均误差最小的
k值，当然还可以将俩种方法的有点相结合，选出理想的k值。
'''
import numpy as np
import operator
from os import listdir
import numpy as np
#准备数据：将图像转换为测试向量
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
#print(img2vector('digits/testDigits/0_1.txt'))

#分析数据
def classify0(inX, dataSet, labels, k):

    """
    参数:
    - inX: 用于分类的输入向量
    - dataSet: 输入的训练样本集
    - labels: 样本数据的类标签向量
    - k: 用于选择最近邻居的数目
    """

    # 获取样本数据数量
    dataSetSize = dataSet.shape[0]

    # 矩阵运算，计算测试数据与每个样本数据对应数据项的差值
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet

    # sqDistances 上一步骤结果平方和
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)

    # 取平方根，得到距离向量
    distances = sqDistances**0.5

    # 按照距离从低到高排序
    sortedDistIndicies = distances.argsort()
    classCount = {}

    # 依次取出最近的样本数据
    for i in range(k):
        # 记录该样本数据所属的类别
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # 对类别出现的频次进行排序，从高到低
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True)

    # 返回出现频次最高的类别
    return sortedClassCount[0][0]

#测试算法
def handwritingClassTest():
    # 样本数据的类标签列表
    hwLabels = []

    # 样本数据文件列表
    trainingFileList = listdir('digits/trainingDigits')
    m = len(trainingFileList)

    # 初始化样本数据矩阵（M*1024）
    trainingMat = np.zeros((m, 1024))

    # 依次读取所有样本数据到数据矩阵
    for i in range(m):
        # 提取文件名中的数字
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)

        # 将样本数据存入矩阵
        trainingMat[i, :] = img2vector(
            'digits/trainingDigits/%s' % fileNameStr)

    # 循环读取测试数据
    testFileList = listdir('digits/testDigits')

    # 初始化错误率
    errorCount = 0.0
    mTest = len(testFileList)

    # 循环测试每个测试数据文件
    for i in range(mTest):
        # 提取文件名中的数字
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])

        # 提取数据向量
        vectorUnderTest = img2vector('digits/testDigits/%s' % fileNameStr)

        # 对数据文件进行分类
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)

        # 打印 K 近邻算法分类结果和真实的分类
        print("测试样本 %d, 分类器预测: %d, 真实类别: %d" %
              (i+1, classifierResult, classNumStr))

        # 判断K 近邻算法结果是否准确
        if (classifierResult != classNumStr):
            errorCount += 1.0

    # 打印错误率
    print("\n错误分类计数: %d" % errorCount)
    print("\n错误分类比例: %f" % (errorCount/float(mTest)))

print(handwritingClassTest())