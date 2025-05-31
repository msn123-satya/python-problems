'''#row-wise sum in a matrix
l=[[int(input())for q in range(3)]for p in range(3)]
print(l)
rs=[]
for p in range(3):
    s1=0
    for q in range(3):
        s1=s1+l[p][q]
    rs.append(s1)
print(rs)

#column wise sum in a matrix
l=[[int(input())for q in range(3)]for p in range(3)]
print(l)
cs=[]
for p in range(3):
    s1=0
    for q in range(3):
        s1=s1+l[q][p]
    cs.append(s1)
print(cs)

l=[]#[[1,2,3],[4,5,6],[7,8,9]]
for p in range(3):
    row=list(map(int,input().split()))[:3]
    l.append(row)
for p in range(3):
    for q in range(3):
        print(l[p][q],end=" ")
    print()
le=len(l)-1
s1=0
s2=0
for p in range(3):
    for q in range(3):
        if(p==q):
            s1=s1+l[p][q]
        if(le==(p+q)):
            s2=s2+l[p][q]
print(s1)
print(s2)

l=[]#[[1,2,3],[4,5,6],[7,8,9]]
for p in range(3):
    row=list(map(int,input().split()))[:3]
    l.append(row)
for p in range(3):
    for q in range(3):
        print(l[q][p],end=" ")
    print()

l=[]#[[1,2,3],[4,5,6],[7,8,9]]
for p in range(3):
    row=list(map(int,input().split()))[:3]
    l.append(row)
for p in l:
    for q in p[::-1]:
        print(q,end=" ")
    print()

l=[]#[[1,2,3],[4,5,6],[7,8,9]]
for p in range(3):
    row=list(map(int,input().split()))[:3]
    l.append(row)
for p in l[::-1]:
    for q in p:
        print(q,end=" ")
    print()

l=[]#[[1,2,3],[4,5,6],[7,8,9]]
for p in range(3):
    row=list(map(int,input().split()))[:3]
    l.append(row)
for p in l[::-1]:
    for q in p[::-1]:
        print(q,end=" ")
    print()'''


    

        
