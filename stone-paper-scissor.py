import random
def search(e,l):
    flag=0
    for i in range(len(l)):
        if(e==l[i]):
            flag=1
            break
    return flag
while True:
    l1=[]
    l2=[]
    for i in range(8):
        l1.append(random.randint(0,100))
        l2.append(random.randint(0,100))
    print("Player 1 :[",l1,"]\n")
    print("Player 2 :[",l2,"]\n")
    p1=int(input("Player 1: (Pick a number from the list.) "))
    p2=int(input("Player 2: (Pick a number from the list.) "))
    if(search(p1,l1)==0):
        print("\nPlayer 1 didn't enter correctly.\n")
        continue
    else:
        if(search(p2,l2)==0):
            print("\nPlayer 2 didn't enter correctly.\n")
            continue
        else:
            if(p1%2==0):print("Player 1: STONE\n")
            elif(p1%3==0):print("Player 1: PAPER\n")
            else:print("Player 1: SCISSOR\n")
            if(p2%2==0):print("Player 2: PAPER\n")
            elif((p2%3)==0):print("Player 2: SCISSOR\n")
            else:print("Player 2: STONE\n")
            if(p1%2==0 and p2%2==0):print("Player 2 wins")
            elif(p1%2==0 and p2%3==0):print("Player 1 wins")
            elif(p1%2==0):print("Draw")
            elif(p1%3==0 and p2%2==0):print("Draw")
            elif(p1%3==0 and p2%3==0):print("Player 2 wins")
            elif(p1%2==0):print("Player 1 wins")
            elif(p2%2==0):print("Player 1 wins")
            elif(p2%3==0):print("Draw")
            else:print("Player 2 wins")
    k=input("Press C to continue.")
    if(k!='C' and k!='c'):break
