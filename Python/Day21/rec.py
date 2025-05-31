#i/p:abcde o/p:12a1b1c2d3e5
'''s=input()
l=len(s)
ln=[]
i=1
a=1
b=0
while(i<=l):
    c=a+b
    ln.append(c)
    a=b
    b=c
    i=i+1
s1=str(sum(ln))
res=''
res=res+s1
for p in range(l):
    res=res+s[p]+str(ln[p])
print(res)'''

#i/p:11,15 o/p=4;no.of non-duplicate numbers
'''def num_range(n):
    l=[]
    while(n!=0):
        r=n%10
        if r in l:
            return 0
        l.append(r)
        n=n//10
    return 1
n1=int(input())
n2=int(input())
c=0
for p in range(n1,n2+1):
    d=num_range(p)
    c=c+d
print(c)'''

#i/p:5   [1,4,2,1,4]  ,o/p: 1(as the 2 dup ele 1,4;1 has less index than 4)
#i/p:6   [1,4,0,2,3,5],o/p:-1(as no dup ele)
'''n=int(input())
l=list(map(int,input().split()))[:n]
for p in l:
    if(l.count(p)>1):
        print(p)
        break
else:
    print("-1")'''

#1 2 3 2 4 2 5 2, remove 2----> [1,3,4,5]
'''l=list(map(int,input().split()))
n=int(input())
r=[x for x in l if x!=n]
print(r)
#or
l=list(map(int,input().split()))
n=int(input())
c=l.count(n)
for p in range(c):
    l.remove(n)
print(l)'''

#i/p:7  52,66,64,36,45,24,32;o/p:207 (sum of leader ele=66+64+45+32=207)
'''n=int(input())
l=list(map(int,input().split()))[:n]
r=[]
for p in range(len(l)-1):
    for q in range(p+1,len(l)):
        if(l[q]>l[p]):
            break
    else:
        r.append(l[p])
print(sum(r)+l[-1])'''


