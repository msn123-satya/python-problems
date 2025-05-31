#i/p:cat batman latt matter cat matter cat cat latt latt
#3
#o/p:cat latt 
'''s=input().split()
n=int(input())
d={p:s.count(p) for p in s if s.count(p)>=n}
print(d)
for p,q in d.items():
    print(p,end=" ")'''

#car speeds
'''n1=int(input())
n2=int(input())
x=int(input())
if n2<=n1:
    print(-1)
else:
    sec=x//(n2-n1)
    c_s=sec+1
    print(c_s)'''

'''s1=int(input())
s2=int(input())
d=int(input())
c1=d
c2=0
t=0
if(s1>=s2):
    print(-1)
else:
    while(c1>=c2):
        c1=c1+s1
        c2=c2+s2
        t=t+1
    print(t)'''

