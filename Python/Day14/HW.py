'''n=int(input())
l=list(map(int,input().split()))[:n]
r=[]
l.sort()
for p in range(len(l)//2):
    r.append(l[p])
    r.append(l[-(p+1)])
if(len(l)%2!=0):
    r.append(l[len(l)//2])
print(*r)'''


n=int(input())
l=list(map(int,input().split()))[:n]
num=int(input())
diff=int(input())
c=0
for p in l:
    d=abs(p-num)
    if(d<=diff):
       c=c+1
print(c)

