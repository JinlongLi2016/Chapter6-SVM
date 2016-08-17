from random import random

def loadDataSet(filename):
    '''

    :param filename:
    :return:
    '''
    dataMat = []; labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

def selectJrand(i, m):
    '''

    :param i:
    :param m:
    :return:
    '''
    j = i
    while (j==i):
        j = int(random.uniform(0, m))
    return  j

def clipAlpha(aj, H, L):
    '''

    :param aj:
    :param H:
    :param L:
    :return:
    '''
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj