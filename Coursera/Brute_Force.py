import os
import time

# Graph Matrix
#G = [[0,1,0,1,0],[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,0]]

def ReadGraphFromFile(name):
    workingDir = os.getcwd() + "\\"   
    try:
        file = open(workingDir + name, "r")
        size = 0 
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
    except FileNotFoundError:
        print("Graph Dosyası Bulunamadı ... ")
        input("Geri Dönmek İçin 'enter'a Basınız...\n")
        return []

def WriteGraphToFile(G,name):
    workingDir = os.getcwd() + "\\"   
    file = open(workingDir + name, "w")
    write_str = ""
    for i, subG in enumerate(G):
        for j, val in enumerate(subG):
            if val == 1:
                write_str += str(i) + " " + str(j) + "\n"
    #write_str += "\n"
    print(write_str)
    file.write(write_str)
    file.close()

def PrintGraph(G):
    for i,subG in enumerate(G):
        print(i,end=" || ")
        for j,val in enumerate(subG):
            print(val,end=" | ")
        print()
        print(len(G)*5*"-")
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
    print("[1] - Grafiği Görüntüle")
    print("[2] - Dosyadan Graph Bilgilerini Al")
    print("[3] - Graph Bilgilerini Text Dosyasına Yaz")
    print("[4] - Bir noktadan diğerine yol bul...")
    print("[5] - Bir noktanın derecesini bul...")
    print("[6] - Küçük Dünya mı?")
    print("")
    print("[0] - Çıkış...")
    selection = input("Lütfen Seçiminizi Yapınız... \n")
    return selection
    
def Main():
    G = []
    while True:
        os.system("cls")
        selection = Menu()
        os.system("cls")
        if selection == "1":
            if G == []:
                print("Graph BOŞ")
                input("Geri Dönmek İçin 'enter'a Basınız...\n")
            else:
                PrintGraph(G)
        elif selection == "2":
            os.system("dir")
            fileName = input("Veri Alınacak Dosya İsmi Giriniz\n")
            if fileName != "":
                G = ReadGraphFromFile(fileName)
            else:
                print("Lütfen Dosya Adı Veriniz")
                input("Geri Dönmek İçin 'enter'a Basınız...\n")
        elif selection == "3":
            fileName = input("Yazılacak Dosya İsmi Giriniz\n")
            if G == []:
                print("G Matrisi Boş. Kaydedilecek Birşey Yok...")
                input("Geri Dönmek İçin 'enter'a Basınız...\n")
            else:
                WriteGraphToFile(G, fileName)
        elif selection == "4":
            startNode = int(input("Başlangıç Noktasını Giriniz...\n"))
            endNode = int(input("Bitiş Noktasını Giriniz...\n"))
            #G = ReadGraphFromFile("gr1.txt")
            FindWay(G,startNode,endNode)
            input("Geri Dönmek İçin 'enter'a Basınız...\n")
        elif selection == "5":
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


