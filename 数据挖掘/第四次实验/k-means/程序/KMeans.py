from numpy import *
import matplotlib.pyplot as plt
#导入数据
def loadDataSet(fileName):
    dataSets = []
    data = []
    f = open(fileName)
    for line in f.readlines():
        curLine = line.strip().split('\t')
        x = float(curLine[0])
        y = float(curLine[1])
        dataSets.append([x,y])
    return mat(dataSets)
#计算距离
def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))
#随机生成k个点作为初始质心
def randCent(dataSet, k):
    n = shape(dataSet)[1] #n是列数
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j]) #找到第j列最小值
        rangeJ = float(max(dataSet[:, j]) - minJ) #求第j列最大值与最小值的差
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1) #生成k行1列的在(0, 1)之间的随机数矩阵
    return centroids
#K均值聚类算法实现
def KMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = shape(dataSet)[0] #数据集的行
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m): #遍历数据集中的每一行数据
            minDist = inf;minIndex = -1
            for j in range(k): #寻找最近质心
                distJI = distMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist: #更新最小距离和质心下标
                    minDist = distJI; minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2 #记录最小距离质心下标，最小距离的平方
        print(centroids)
        for cent in range(k): #更新质心位置
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]] #获得距离同一个质心最近的所有点的下标，即同一簇的坐标
            centroids[cent,:] = mean(ptsInClust, axis=0) #求同一簇的坐标平均值，axis=0表示按列求均值
    return centroids, clusterAssment
#绘制散点图
def showCluster(dataSet, k, clusterAssment, centroids):
    fig = plt.figure()
    plt.title("K-means")
    ax = fig.add_subplot(111)
    data = []
    for cent in range(k): #提取出每个簇的数据
        ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]] #获得属于cent簇的数据
        data.append(ptsInClust)
    for cent, c, marker in zip( range(k), ['r', 'g', 'b', 'y'], ['^', 'o', '*', 's'] ): #画出数据点散点图
        ax.scatter(array(data[cent][:, 0]), array(data[cent][:, 1]), s=80, c=c, marker=marker)
    ax.scatter(array(centroids[:, 0]), array(centroids[:, 1]), s=1000, c='black', marker='+', alpha=1) #画出质心点
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plt.show()
def main():
    dat = mat(loadDataSet('Test_data.txt'))  # 读入数据
    center, clust = KMeans(dat, 4)
    randCent(dat,4)
    showCluster(dat, 4, clust, center)
if __name__ == "__main__":
    main()