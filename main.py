#!/usr/local/bin/python3
def classify(x, k, training_x, training_y):
    def distance(a, b):
        return sum([(c-d)**2 for c,d in zip(a, b)])
    nearest = list(zip(training_x, training_y)).sort(key=lambda y: distance(fst(y),x))[:k]
    ys=[b for a,b in nearest]
    if sum(ys)>(len(ys)/2):
        return 1
    else:
        return 0


from sys import stdin

for line in stdin:
    if line == '': 
        break
    d=[float(x) for x in line.split(',')]
    print(1)


