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

perms = []
tempList = []

def addperm(values,tempList):
    a = 0
    for i in tempList:
        for q in range(len(values)):
            j = values[a]
            a += 1
            i.append(j)

def perm2(values,leng):
    for i in values:
        for j in range(len(values)):
            tempList.append([i])
    for i in range(leng-1):
        addperm(values,tempList)

    return tempList

perm2([1,2,3,4],2)
print(tempList)








def CreatePermutations(perms, values, maxLen):
    perms = []
    tempList = []
    for i in values:
        perms.append(i)
    for i in values:
        for j in values:
            if i != j:
                tempList.append(i)
                perms.append(tempList)

    return perms

