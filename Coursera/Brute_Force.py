G = [[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]

def PrintGraph(G):
    for i in G:
        print(i)
    
def FindWay(G,i,j):
    betweenValues = []
    for a in range(len(G)):
        betweenValues.append(a)
    betweenValues.remove(i)
    betweenValues.remove(j)
    print(betweenValues)
    maxPermLen = len(betweenValues)
    perms = []
    perms = CreatePermutations(perms, betweenValues, maxPermLen)
    print(perms)

def CreatePermutations(perms, values, maxLen):
    if len(values) == maxLen:
        for i in values:
            perms.append(i)
    maxLen -= 1
    return perms


FindWay(G,1,3)