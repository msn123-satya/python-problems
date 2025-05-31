'''#passing lambda into other functions
def operations(a,b,s):
    r=s(a,b)
    return r
s=operations(20,10,lambda a,b:a+b)
d=operations(20,10,lambda a,b:a-b)
m=operations(20,10,lambda a,b:a*b)
print(s,d,m)

#with filter and without lambda
def even(n):
    if n%2==0:
        return n
l=[1,2,3,4,5,6]
r=list(filter(even,l))
print(r)

#with filter and with lambda
l=[1,2,3,4,5,6]
r=list(filter(lambda n:n%2==0,l))
print(r)

#l=[-1,-2,3,-4,6,-6,-7] filter +ve number using filter with lambda and without lambda
def  positive(n):
    if n>0:
        return n
l=[-1,-2,3,-4,6,-6,-7]
r=list(filter(positive,l))
print(r)

#with filter and with lambda
l=[-1,-2,3,-4,6,-6,-7]
r=list(filter(lambda n:n>0,l))
print(r)

#find squares with map and without lambda
def sq(n):
    return n*n
l=[1,2,3,4,5,6]
r=list(map(sq,l))
print(r)

#with map and with lambda
l=[1,2,3,4,5,6]
r=list(map(lambda x:x*x,l))
print(r)

#find cubes with map and without lambda
def cube(n):
    return n*n*n
l=[1,2,3,4,5,6]
r=list(map(cube,l))
print(r)

#with map and with lambda*
l=[1,2,3,4,5,6]    
r=list(map(lambda x:x*x*x,l))
print(r)

#reduce with lambda addition
from functools import reduce
s=[1,2,3,4,5]
l=reduce(lambda a,b:a+b,s)
print(l)

#reduce with lambda multiplication
from functools import reduce
s=[1,2,3,4,5]
l=reduce(lambda a,b:a*b,s)
print(l)

#max number using reduce function
from functools import reduce
s=[16,2,35,47,58,78,98]
l=reduce(lambda a,b:a if (a>b) else b,s)
print(l)

#min number using reduce function
from functools import reduce
s=[16,2,35,47,58,78,98]
l=reduce(lambda a,b:a if (a<b) else b,s)
print(l)'''

'''#generator
def gen():
    '''yield 5
    yield 10
    yield 15
    yield 20'''
    l=[5,10,15,20]
    for p in l:
        yield p
g1=gen()
'''a=next(g1)
b=next(g1)
c=next(g1)
d=next(g1)'''
print(a,b,c,d)
for p in g1:
    print(p,end=" ")
     
#multiple random numbers
import random
def otp():
    i=1
    while(i<=3):
        r=random.randint(1000,9999)
        yield r
        i=i+1
o=otp()
'''for p in o:
    print(p)'''
a,b,c=next(o),next(o),next(o)
print(a,b,c)'''











    
