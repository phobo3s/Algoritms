import os
import time

# Graph Matrix
#G = [[0,1,0,1,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,0]]

def ReadGraphFromFile(name):
    workingDir = os.getcwd() + "\\"   
    try:
        size = 0
        file = open(workingDir + name, "r") 
        connections = file.readlines()
        for i in range(len(connections)):
            connections[i] = connections[i].replace("\n","").split(" ")
            connections[i][0] = int(connections[i][0])
            connections[i][1] = int(connections[i][1])
            if size < connections[i][0]:
                size = connections[i][0]
            elif size < connections[i][1]:
                size = connections[i][1]
            else:
                pass
        file.close()
        G = []
        # Make Zero Array
        for x in range(size+1):
            G.append([])
            for y in range(size+1):
                G[x].append([])
                G[x][y] = 0
        for i in connections:
            G[i[0]][i[1]] = 1
        input("Yükleme Tamamlandı 'enter'a Basınız...\n")
        return G
    except FileExistsError:
        print("Graph Dosyası Bulunamadı ... ")
        input("Geri Dönmek İçin 'enter'a Basınız...\n")

def WriteGraphToFile(G,name):
    workingDir = os.getcwd() + "\\"   
    file = open(workingDir + name, "w")
    
    file.write()




    file.close()

def PrintGraph(G):
    for i in G:
        print(i)
    input("Geri Dönmek İçin 'enter'a Basınız...\n")
    
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

def Menu():
    print(50*"=")
    print("[1] - Dosyadan Graph Bilgilerini Al")
    print("[2] - 1")
    print("[3] - Bir noktadan diğerine yol bul...")
    print("[4] - Bir noktanın derecesini bul...")
    print("[5] - Küçük Dünya mı?")
    print("")
    print("[0] - Çıkış...")
    selection = input("Lütfen Seçiminizi Yapınız... \n")
    return selection
    
def Main():
    while True:
        os.system("cls")
        selection = Menu()
        if selection == "1":
            G = ReadGraphFromFile("gr1.txt")
            PrintGraph(G)
        elif selection == "3":
            startNode = int(input("Başlangıç Noktasını Giriniz...\n"))
            endNode = int(input("Bitiş Noktasını Giriniz...\n"))
            #G = ReadGraphFromFile("gr1.txt")
            FindWay(G,startNode,endNode)
            input("Geri Dönmek İçin 'enter'a Basınız...\n")
        elif selection == "4":
            pass
        elif selection == "0":
            print("Hoşçakal")
            time.sleep(2)
            os.system("cls")
            break
        else:
            print("Hatalı seçim yaptınız lütfen tekrar deneyiniz...")

if __name__ == "__main__":
    Main()
    pass


#DEPRECATED
def PermCount(values,leng):
    leng -= 1
    a = len(values) -leng 
    if leng != 0:
        pc = a * PermCount(values, leng)
    else:
        pc = len(values)
    return pc


