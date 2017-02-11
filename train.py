# _*_ coding: utf-8 _*_

import nltk
import random

file = open('text/godfather.txt','r',encoding='utf-8')
incise = file.read()
incise = incise.split()

def makePairs(arr):
    pairs = []
    for i in range(len(arr)):
        if i < len(arr) - 1:
            temp = (arr[i],arr[i+1])
            pairs.append(temp)
    return pairs

def generate(cfd,word='the',num=500):
    for i in range(num):
        arr = []
        for j in cfd[word]:
            for k in range(cfd[word][j]):
                arr.append(j)
        print(word,end=' ')

        word = arr[int((len(arr))*random.random())]

pairs = makePairs(incise)
cfd = nltk.ConditionalFreqDist(pairs)
generate(cfd)