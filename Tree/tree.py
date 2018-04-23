from math import log
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

if __name__ == '__main__':
    dataSet=[ [1,1,'yes'],
              [1,1,'yes'], 
              [1,0,'meibi'] ,
              [0,1,'no'] , 
              [0,1,'no'] ]
    a=calcShannonEnt(dataSet)
    print(a)
