# Graph Matrix
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


def PermCount(values,leng):
    leng -= 1
    a = len(values) -leng 
    if leng != 0:
        pc = a * PermCount(values, leng)
    else:
        pc = len(values)
    return pc

def Permutate(values,leng):
    if len(values) == leng+1:
        return values
    permList = []
    for i in values:
        remaining_elements = [x for x in values if x != i]
        z = Permutate(remaining_elements,leng)
        for t in z:
            permList.append([i] + [t])

    return permList
    

perms = Permutate([1,2,9,4],1)

print(perms)

