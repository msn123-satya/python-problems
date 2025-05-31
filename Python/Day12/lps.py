'''#print 2-5 tables in console
s,e=map(int,input("enter s,e numbers:").split())
print(s,e)
for p in range(s,e+1):
    for q in range(1,11):
        print(p,"*",q,"=",p*q)
    print()

#printing prime numbers b/w 1-100
n=int(input("enter n:"))
c1=0
for p in range(2,n+1):
    c=0
    for q in range(1,p+1):
        if(p%q==0):
            c=c+1
    if(c==2):
        print(p,end=" ")
        c1=c1+1
print()
print("count:",c1)

#printing armstrong number b/w 1-1000
n=int(input("enter n:"))
for p in range(1,n+1):
    m=p
    for q in range(1,p+1):
        s=0
        while(q!=0):
            r=q%10
            s=s+(r*r*r)
            q=q//10
    if(s==m):
        print(m,end=" ")
print()

#or

n=int(input("enter n:"))
c1=0
for p in range(1,n+1):
    m=p
    s=0
    while(p!=0):
        r=p%10
        s=s+(r*r*r)
        p=p//10
    if(s==m):
        print(m,end=" ")
        c1=c1+1
print()
print("count:",c1)

#[23,34,62,75,89,91]------>input
#[5,7,8,12,17,10]--------->output
res=[]
l=[23,34,62,75,89,91]
for p in l:
    s=0
    while(p!=0):
        r=p%10
        s=s+r
        p=p//10
    res.append(s)
print(res)

#50-55 print sum of the numbers of the digits in b/w the numbers((5+0)+(5+1)+(5+2)+(5+3)+(5+4)+(5+5))=45
s,e=map(int,input("enter s,e:").split())
res=[]
for p in range(s,e+1):
    s=0
    while(p!=0):
        r=p%10
        s=s+r
        p=p//10
    res.append(s)
print(sum(res))

#or

s,e=map(int,input("enter s,e:").split())
s1=0
for p in range(s,e+1):
    s=0
    while(p!=0):
        r=p%10
        s=s+r
        p=p//10
    s1=s1+s
print(s1)'''


    






