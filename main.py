from sklearn.neighbors import KNeighborsClassifier
from sys import stdin
import pandas as pd

WINDOWSIZE=5 # windowsize input 
K=10 # K parameter for KNN algorithm  

# load training data
data = list(pd.read_csv('training.csv')['LogReturns'])

# convert time series into training examples
x_train = []
y_train = []
for i in range(len(data)-WINDOWSIZE):
    x_train.append(data[i:i+WINDOWSIZE])
    y_train.append(round(data[i+WINDOWSIZE]))

# declare and train classifier
classifier=KNeighborsClassifier(n_neighbors=K)
classifier.fit(x_train, y_train)

# classify terminal input
for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    print(classifier.predict([d])[0])


