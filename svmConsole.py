import svmMLiA

dataArr, labelArr = svmMLiA.loadDataSet('testSet.txt')
print('labelArra = ', labelArr)

b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print('b=',b)
print('alphas=', alphas)