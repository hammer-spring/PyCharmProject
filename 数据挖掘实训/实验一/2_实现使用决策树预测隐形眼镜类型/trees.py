# coding:utf-8
from math import log
import operator
import treePlotter
"""
计算香农熵
"""
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    #为所有可能分类创建字典
    for featVec in dataSet: #the the number of unique elements and their occurance
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    #以2为底求对数, prob为选择该分类的概率
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt

"""
按照给定特征划分数据集
输入：dataSet-待划分数据集
     axis-划分数据集特征
     value-特征返回值
"""
def splitDataSet(dataSet, axis, value):          #会把dataSet[axis]==value的那些组数据保留（并去除value值）
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

"""
选择最好的数据集划分方式
"""
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:      #uniqueVals中保存的是我们某个样本的特征值的所有的取值的可能性
            subDataSet = splitDataSet(dataSet, i, value)
            # 在这里划分数据集，比如说第一个特征的第一个取值得到一个子集，第一个特征的特征又会得到另一个特征。当然这是第二次循环
            # 我们以第一个特征来说明，根据第一个特征可能的取值划分出来的子集的概率
            prob = len(subDataSet)/float(len(dataSet))
            # 根据这个代码就可以计算出划分子集的熵（数学期望）
            newEntropy += prob * calcShannonEnt(subDataSet)
        # 计算出信息增益
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature                      #returns an integer

"""
返回出现次数最多的分类名称
"""
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


"""
递归构建决策树
"""
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]  #classList保存标签
    if classList.count(classList[0]) == len(classList):
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)   # 得到列表包含所有属性值
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree

if __name__ == '__main__':
    # del表示删除，与remove区别如下
    nums = [1,0, 2 ,0 ,3,0,0]
    nums.remove(0)
    print (nums) #[1, 2, 0, 3, 0, 0]
    del(nums[0])
    print(nums)

    # 预测隐形眼镜类型
    fr=open('lenses.txt')
    lenses=[inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels=['age', 'prescript', 'astigmatic', 'tearRate']
    lensesTree=createTree(lenses, lensesLabels)
    print (lensesTree)
    treePlotter.createPlot(lensesTree)  #绘图,treePlotter.py文件如下
