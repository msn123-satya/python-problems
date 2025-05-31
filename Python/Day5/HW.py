'''#strong number
import math
n=int(input())
s=0
m=n
while(n!=0):
    r=n%10
    s=s+(math.factorial(r))
    n=n//10
if(m==s):
    print("YES")
else:
    print("NO")

#factorial
import math
n=int(input())
while(n>=0):
    f=math.factorial(n)
    print(f,"is the factorial of the number")
    break

#printing 5th table
n=int(input())
i=0
while(i<=9):
    i=i+1
    print(n,"*",i,"=",n*i)

#odd digit and even digit sum
n=int(input("Enter a number:"))
s=0
es=0
os=0
while(n!=0):
    r=n%10
    s=s+r
    if(r%2==0):
        es=es+r
    else:
        os=os+r
    n=n//10
print("Sum of all digits:",s)
print("Sum of even digits:",es)
print("Sum of odd digits:",os)'''
