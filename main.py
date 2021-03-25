#!/usr/local/bin/python3
from sklearn.neighbors import KNeighborsClassifier

def classify(x, k, training_x, training_y):
    def distance(a, b):
        return sum([(c-d)**2 for c,d in zip(a, b)])
    nearest = list(zip(training_x, training_y)).sort(key=lambda y: distance(y[0],x))[:k]
    ys=[b for a,b in nearest]
    if sum(ys)>(len(ys)/2):
        return 1
    else:
        return 0


from sys import stdin
import pandas as pd
WINDOWSIZE=5
data = list(pd.read_csv('LatencyChallengeTraining.csv')['Log Returns'])
x_train = []
y_train = []
for i in range(len(data)-WINDOWSIZE):
    x_train.append(data[i:i+WINDOWSIZE])
    y_train.append(round(data[i+WINDOWSIZE]))
#print(x_train)
#print(None in x_train)
#for i in zip(x_train,y_train):
#    print(i)
#for i in map(lambda x: x[0], zip(x_train,y_train)):
#    print(i)
classifier=KNeighborsClassifier(n_neighbors=10)
classifier.fit(x_train, y_train)
for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    print(classifier.predict([d])[0])


