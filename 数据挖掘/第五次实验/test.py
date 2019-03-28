import logRegres
dataArr,labelMat=logRegres.loadDataSet()
a = logRegres.gradAscent(dataArr,labelMat)
print a

from numpy import *
reload(logRegres)
print logRegres.plotBestFit(a.getA())

'''
weights = logRegres.stocGradAscent0 (array(dataArr),labelMat)
print logRegres.plotBestFit(weights)
'''

weights = logRegres.stocGradAscent1 (array(dataArr),labelMat)
print logRegres.plotBestFit(weights)
