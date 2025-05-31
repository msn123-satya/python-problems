'''s=[[1,2,3],[4,5,6],[7,8,9]]
print(s)
print(len(s))
print(len(s[0]))
for p in s:
    print(p)
for p in s:
    print(p)
    for q in p:
        print(q)
s1=0
for p in s:
    for q in p:
        s1=s1+q
print("sum:",s1)
s2=0
for p in s:
    s2=s2+sum(p)
print(s2)

nl=[]
for p in range(3):
    l=[]
    for q in range(3):
        ele=int(input("Enter value:"))
        l.append(ele)
    nl.append(l)
print(nl)
for p in range(3):
    for q in range(3):
        print(nl[p][q],end=" ")
    print()

nl=[]
for p in range(3):
    l=[]
    for q in range(2):
        ele=int(input("Enter value:"))
        l.append(ele)
    nl.append(l)
print(nl)
for p in range(3):
    for q in range(2):
        print(nl[p][q],end=" ")
    print()

nl=[[int(input("Enter value:")) for q in range(3)]for p in range(3)]
print(nl)
for p in range(3):
    for q in range(3):
        print(nl[p][q],end=" ")
    print()


m=int(input("Enter no.of students:"))
n=int(input("Enter no.of subjects:"))
nl=[]
for p in range(m):
    m=[]
    for q in range(n):
        marks=int(input("Enter marks:"))
        m.append(marks)
    nl.append(m)
print(nl)
i=0
res=0
for p in nl:
    for q in p:
        if(q<35):
            break
    else:
        res=1
    print("student",i+1,"pass") if(res==1) else print("student",i+1,"fail")
    i=i+1

m=int(input("Enter no.of students:"))
n=int(input("Enter no.of subjects:"))
nl=[]
for p in range(m):
    m=[]
    for q in range(n):
        marks=int(input("Enter marks:"))
        m.append(marks)
    nl.append(m)
print(nl)
i=0
res=1
for p in nl:
    for q in p:
        if(q<35):
            res=0
            break
    else:
        res=1
    print("student",i+1,"pass") if(res==1) else print("student",i+1,"fail")
    i=i+1
    if(res==1):
        total=sum(p)
        avg=total/n
        print(total,avg)

l=[[int(input("Enter value:")) for q in range(2)]for p in range(2)]
print(l)
r=[[int(input("Enter value:")) for q in range(2)]for p in range(2)]
print(r)
a=[]
for p in range(2):
    d=[]
    for q in range(2):
        s=l[p][q]+r[p][q]
        d.append(s)
    a.append(d)
print(a)'''

l=[[int(input("Enter value:")) for q in range(2)]for p in range(2)]
print(l)
r=[[int(input("Enter value:")) for q in range(2)]for p in range(2)]
print(r)
a=[]
for p in range(2):
    d=[]
    for q in range(2):
        s=l[p][q]-r[p][q]
        d.append(s)
    a.append(d)
print(a)


