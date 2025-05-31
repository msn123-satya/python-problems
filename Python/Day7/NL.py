'''#max and min in a num
n=int(input())
max1=0
min1=9
while(n!=0):
    r=n%10
    if(r>max1):
        max1=r
    if(r<min1):
        min1=r
    n=n//10
print("max:",max1)
print("min:",min1)

#43197---->even index sum=12,odd index sum=12
n=int(input())
ei=0
oi=0
s=str(n)
l=len(s)-1
while(n!=0):
    r=n%10
    if(l%2==0):
        ei=ei+r
    else:
        oi=oi+r
    l=l-1
    n=n//10
print("Sum of even index:",ei)
print("Sum of odd index:",oi)

#4322417---->print digit count
#4 count 2 #1 count 1
#3 count 1 #7 count 1
#2 count 2
n=int(input())
l=list(map(int,str(n)))
l.sort()
d={p:l.count(p) for p in l}
for p,q in d.items():
    print(p,"count",q)

#123--->input
#1111011---->output
n=int(input())
l=[]
while(n!=0):
    r=n%2
    l.append(r)
    n=n//2
l.reverse()
s=list(map(str,l))
print(''.join(s))

#scholarship
marks=list(map(int,input().split()))
print(marks)
s=sum(marks)
a=s/len(marks)
max1=max(marks)
min1=min(marks)
if ((min1>=2) and (max1==5) and (a>=4)):
    print("YES")
else:
    print("NO")

n=int(input("enter n:"))
if(-32678<=n<=32767):
    temp=n
    if(n<0):
        n=n*-1
    s=0
    while(n!=0):
        r=n%10
        s=(s*10)+r
        n=n//10
    if(temp<0):
        s=s*-1
    print(s)
else:
    print("Wrong value")

#even place replace 1
#odd place replace 0
n=int(input())
l=list(map(int,input().split()))[:n]
for p in range(len(l)):
    if(l[p]%2==0):
        l[p]=1
    else:
        l[p]=0
print(*l)

#missing characters
#lower case
s=input()
r=''
for p in range(97,123):
    d=chr(p)
    if d not in s:
        r=r+d
if(len(r)>0):
    print(r)
else:
    print(0)
    
#upper case missing characters   
s=input()
r=''
for p in range(65,90):
    d=chr(p)
    if d not in s:
        r=r+d
if(len(r)>0):
    print(r)
else:
    print(0)'''






    
