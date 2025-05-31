print("***************EVM****************")
tc=0
yc=0
cc=0
pc=0
nc=0
while(True):
    print("1.TDP/JSP/BJP,2.YSRCP,3.CONGRESS,4.PRAJASHANTI,5.NOTA")
    opt=int(input("enter your vote:"))
    match(opt):
        case 1:tc=tc+1
        case 2:yc=yc+1
        case 3:cc=cc+1
        case 4:pc=pc+1
        case 5:nc=nc+1
    opt1=input("Do you want  to continue:y/n")
    if(opt1=="y"):
        continue
    else:
        break
print("TDP:",tc,"YSRCP:",yc,"CONGRESS:",cc,"PRAJASHANTI:",pc,"NOTA:",nc)
m=max(tc,yc,cc,pc,nc)
if(m==tc):
    print("TDP is winner")
elif(m==yc):
     print("YSRCP is winner")
elif(m==cc):
     print("CONGRESS is winner")
elif(m==pc):
     print("PRAJASHANTI is winner")
else:
     print("NOTA")

     
