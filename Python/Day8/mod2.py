'''#normal import
import math
import mod1
a,b=map(int,input("a,b").split())
mod1.add(a,b)
mod1.sub(a,b)
mod1.even_odd(a)
print(math.pi)
s=math.sqrt(a)
m=math.factorial(a)
print(s,m)

#alias name
import math as m
import mod1 as d
a,b=map(int,input("a,b").split())
d.add(a,b)
d.sub(a,b)
d.even_odd(a)
print(m.pi)
s=m.sqrt(a)
m=m.factorial(a)
print(s,m)'''

#from import
from math import*
from mod1 import*
a,b=map(int,input("a,b").split())
su=add(a,b)
diff=sub(a,b)
print(su,diff)
e=even_odd(a)
print("Even") if (e==1) else print("Odd")
print(pi)
m=sqrt(a)
f=factorial(a)
print(m,f)
print(s)



