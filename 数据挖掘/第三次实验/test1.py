import bayes
listOPosts,lisClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
print myVocabList
a=bayes.setOfWords2Vec(myVocabList,listOPosts[0])
print a
b=bayes.setOfWords2Vec(myVocabList,listOPosts[3])
print b

from numpy import *
reload(bayes)
listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)
myVocabList = bayes.createVocabList(listOPosts)
trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
p0V,p1V,pAb=bayes.trainNB0(trainMat,listClasses)
print pAb
print p0V
print p1V

reload(bayes)
c=bayes.testingNB()
print c
