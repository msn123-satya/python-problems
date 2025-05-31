print("****************HOTEL MANAGEMENT****************")
ic=0
pc=0
dc=0
cc=0
tc=0
n=0
while(True):
    print("1.IDLI - Rs20 , 2.PURI - Rs30 , 3.DOSA - Rs35 , 4.CHAPATHI - Rs30 , 5.TEA - Rs10")
    opt=int(input("What do you want to eat:"))
    if opt==1:
        n=int(input("How many plates of idli?"))
        ic=(ic+20)*n
    elif opt==2:
        n=int(input("How many plates of puri?"))
        pc=(pc+30)*n
    elif opt==3:
        n=int(input("How many plates of Dosa?"))
        dc=(dc+35)*n
    elif opt==4:
        n=int(input("How many plates of Chapathi?"))
        cc=(cc+30)*n
    elif opt==5:
        n=int(input("How many cups of tea?"))
        tc=(tc+10)*n
    else:
        print("invalid option")
    opt1=input("Do you want anything else:y/n")
    if(opt1=="y"):
        continue
    else:
        break
print("********************BILL************************")
print("IDLI",ic,"PURI",pc,"DOSA",dc,"CHAPATHI",cc,"TEA",tc)
total=ic+pc+dc+cc+tc
print("Total bill amount:",total)

