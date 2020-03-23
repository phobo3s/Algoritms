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
    perms = []
    for i in range(len(G)-2):
        perms = Permutate(betweenValues, i+1)
        #for j in perms:
        #for a in range(len(j)):
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
    if leng == 1:
        templist =[]
        for a in values:
            templist.append([a])
        return templist
    permList = []
    for i in values:
        remaining_elements = [x for x in values if x != i]
        z = Permutate(remaining_elements,leng-1)
        for t in z:
            permList.append([i] + t)
    return permList

print(FindWay(G,1,3))
