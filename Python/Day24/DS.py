'''def linear_search(l,key):
    for p in range(len(l)):
        if(l[p]==key):
            return p
    return -1
l=list(map(int,input().split()))
key=int(input())
s=linear_search(l,key)
if(s==-1):
    print("ele not found")
else:
    print("ele found at %d index position"%(s))'''

def binary_search(r,key,l,h):
    while(l<=h):
        m=(l+h)//2
        if(r[m]==key):
            return m
        elif(r[m]<key):
            l=m+1
        else:
            h=m-1
    return -1
r=list(map(int,input().split()))
key=int(input())
r.sort()
low=0
high=len(r)-1
s=binary_search(r,key,low,high)
if(s==-1):
    print("ele not found")
else:
    print("ele found at %d index position"%(s))
