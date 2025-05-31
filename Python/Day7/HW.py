n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
for p in range(min(l),max(l)+1):
    if p not in l:
        print(p,end=" ")
    
