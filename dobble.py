import string
import random


def printcard(l):
    i=0
    for i in range(len(l)):
        print(l[i],end="\t")

#main
k=1
while(k!=0):
    symbols=list(string.ascii_letters)
    card1=[0]*8
    card2=[0]*8
    pos1=random.randint(0,7)
    pos2=random.randint(0,7)    #pos1 and pos2 are the positions of the common alphabet on cards 1 and 2
    same_alfa=random.choice(symbols)
    card1[pos1]=same_alfa
    card2[pos2]=same_alfa
    symbols.remove(same_alfa)
    i=0
    while(i<8):
        if(i!=pos1):
            alfa1=random.choice(symbols)
            symbols.remove(alfa1)
            card1[i]=alfa1
        i=i+1
    i=0
    while(i<8):
        if(i!=pos2):        
            alfa2=random.choice(symbols)
            symbols.remove(alfa2)       
            card2[i]=alfa2        
        i=i+1
    print("Your cards :\n")
    printcard(card1)
    print("\n")
    printcard(card2)
    print("\n")
    try:
        k=int(input("Press 0 to exit :"))
    except:
        k=1
