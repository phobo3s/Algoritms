# Graph Matrix
G = [[0,1,0,1,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0]]

def PrintGraph(G):
    for i in G:
        print(i)
    
def FindWay(G,i,j):
    
    betweenValues = [x for x in range(len(G)) if x != i and x != j]
    
    #print(betweenValues)
    
    # Is there Direct Connection?
    if G[i][j] == 1:
        print(20*"-")
        print("There is 1 leng connection between {} and {}.".format(i,j), flush= True)
        print(20*"-")
        print(20*"*")
        print("The Way Found...")
        print(20*"-")
    else:
        perms = []
        for k in range(1,len(G)-1):
            perms = Permutate(betweenValues, k)
            # Try for k leng
            for perm in perms:
                theWay = []
                theWay = [i] + perm + [j]
                isthereaway = False
                for wayNum in range(len(theWay)-1):
                    if G[theWay[wayNum]][theWay[wayNum+1]] == 1:
                        isthereaway = True
                    else: 
                        isthereaway = False
                        break
                if isthereaway:
                    print(20*"-")
                    print("There is {} leng connection between {} and {}.".format(k+1,i,j), flush= True)
                    print("The Way is : {}".format(theWay),flush = True)
                    print(20*"-")
                    break
                else:
                    pass
            if isthereaway:
                print(20*"*")
                print("The Way Found...")
                print(20*"-")
                break
            else:
                pass
        if isthereaway == False:
            print(20*"*")
            print("NO Way Found...")
            print(20*"-")
                

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

def Main():
    startNode = int(input("Başlangıç Noktasını Giriniz...\n"))
    endNode = int(input("Bitiş Noktasını Giriniz...\n"))
    FindWay(G,startNode,endNode)

if __name__ == "__main__":
    Main()


#DEPRECATED
def PermCount(values,leng):
    leng -= 1
    a = len(values) -leng 
    if leng != 0:
        pc = a * PermCount(values, leng)
    else:
        pc = len(values)
    return pc


