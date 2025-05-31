#letter count
'''s="liril"
#with out dict comp
d={}
for p in s:
    d[p]=s.count(p)
print(d)
#with dict comp
d={p:s.count(p) for p in s}
print(d)'''

#vowels and consonants count
'''s="i love india"
d={p:s.count(p) for p in s if p in "aeiou"}
print(d)
d={p:s.count(p) for p in s if p not in "aeiou" and p!=" "}
print(d)'''

#count of even and odd num in the dict
'''s=[1,2,3,4,1,2]
d={p:s.count(p) for p in s if p%2==0}
print(d)
d={p:s.count(p) for p in s if p%2!=0}
print(d)'''

#i/p:s={abeaicaidao} most frequently vowel o/p:a
'''s=input()
d={p:s.count(p) for p in s if p in "aeiou"}
m=max(d.values())
for p,q in d.items():
    if(q==m):
        print(p)
        break'''

#i/p:bbadbababb most frequent char is b replace with t o/p:ttadtatatt
'''s=input()
d={p:s.count(p) for p in s}
x=input()
l=[]
m=max(d.values())
for p,q in d.items():
    if(q==m):
        l.append(p)
l.sort()
res=''
for p in s:
    if(p==l[0]):
        res=res+x
    else:
        res=res+p
print(res)'''

#I/p:12  1 2 12 13 15 17 26 30 38 45 64 72 comparing with 27 ; O/p: 26(min absolute difference)
#using list
'''def least_diff(l,diff):
    d={p:abs(p-diff) for p in l}
    m=min(d.values())
    min1=0
    for p,q in d.items():
        if(q==m):
            min1=p
    return min1
n=int(input())
l=list(map(int,input().split()))[:n]
d=int(input())
r=least_diff(l,d)
print(r)'''
#using dict
'''def least_diff(l,diff):
    min1=abs(l[0]-diff)
    for p in range(1,len(l)):
        d=abs(l[p]-diff)
        if(d<min1):
            min1=d
            mv=l[p]
    return mv
n=int(input())
l=list(map(int,input().split()))[:n]
d=int(input())
r=least_diff(l,d)
print(r)'''

#i/p:8  2 7 2 3 4 3 2 3  o/p:3(3 occurs 3 times in the list,so 3)
'''n=int(input())
l=list(map(int,input().split()))[:n]
r=[]
d={p:l.count(p) for p in l}
for p,q in d.items():
    if(p==q):
        r.append(p)
        print(p)
print(max(r)) if (len(r)>0) else print("-1")''' 





































