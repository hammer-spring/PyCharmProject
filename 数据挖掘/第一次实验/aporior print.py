import apriori
dataSet=apriori.loadDataSet()
print dataSet
C1=apriori.createC1(dataSet)
print C1
D=map(set,dataSet)
print D
L1,suppData0=apriori.scanD(D,C1,0.5)
print L1

reload (apriori)
L,suppData=apriori.apriori(dataSet)
print L
print L[0]
print L[1]
print L[2]
print L[3]
print apriori.aprioriGen(L[0],2)
L,suppData=apriori.apriori(dataSet,minSupport=0.7)
print L
reload(apriori)
L,suppData=apriori.apriori(dataSet,minSupport=0.5)
rules=apriori.generateRules(L,suppData,minConf=0.7)
print rules
rules=apriori.generateRules(L,suppData,minConf=0.5)
print rules
