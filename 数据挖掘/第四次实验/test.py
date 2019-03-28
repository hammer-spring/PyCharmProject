import kMeans
from numpy import *
datMat=mat(kMeans.loadDataSet('testSet.txt'))
print min(datMat[:,0])
print min(datMat[:,1])
print max(datMat[:,1])
print max(datMat[:,0])
print kMeans.randCent(datMat,2)
print kMeans.distEclud(datMat[0],datMat[1])

reload(kMeans)
datMat=mat(kMeans.loadDataSet('testSet.txt'))
myCentroids,clustAssing=kMeans.kMeans(datMat,4)
print myCentroids

print '二分k-均值聚类测试结果：'
reload(kMeans)
datMat3=mat(kMeans.loadDataSet('testSet.txt'))
print datMat3
centList,myNewAssment=kMeans.biKmeans(datMat3,3)
print myNewAssment
print centList
