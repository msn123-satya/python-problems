'''s=0
def s_d(n):
    global s
    if(n!=0):
        r=n%10
        s=s+r
        s_d(n//10)
        return s
print(s_d(123))'''

#reverse of a number using recurrsion
'''s=0
def r_d(n):
    global s
    if(n!=0):
         r=n%10
         r=(s*10)+r
         r_d(n//10)
         return s
n=int(input("enter n:"))
r=r_n(n)
print(r)
if(r==n):
    print("palindrome")
else:
    print("not a palindrome")'''
    
#reverse of a string and palindrome
'''def rev(s):
    if(len(s)!=0):
        temp=s[0]
        rev(s[1:])
        print(temp,end='')
rev("mpmc")'''

#sum of 1-10 digits
'''s=0
def sd(n):
    global s
    if(n<=10):
        s=s+n
        sd(n+1)
    return s
s=sd(1)
print(s)'''

#sum of 1-20 even numbers
'''s=0
def es(n):
    global s
    if(n<=20):
        s=s+n
        es(n+2)
    return s
s=es(0)
print(s)'''

#print 1-5 numbers using recurission
'''def dis(n):
    if(n<=5):
        print(n)
        dis(n+1)
dis(1)'''

#5-1 numbers
'''def dis(n):
    if(n>=1):
        print(n)
        dis(n-1)
dis(5)'''
#list

'''l=[]
def dis(n):
    if(n<=5):
        l.append(n)
        dis(n+1)
dis(1)
print(l)'''

#[20,18,16,14......2]
'''l=[]
def dis(n):
    if(n>=2):
        l.append(n)
        dis(n-2)
dis(20)
print(l)'''

#sum of even numbers(20-2)
'''s=0
def dis(n):
    global s
    if(n>=2):
        if(n%2==0):
            s=s+n
        dis(n-1)
    return s
print(dis(20))'''

#sum of odd numbers(30-50)
'''s=0
def dis(n):
    global s
    if(n<=50):
        if(n%2!=0):
            s=s+n
        dis(n+1)
    return s
print(dis(30))'''

#5th table using recursion
'''n=int(input("enter n:"))
def table(i):
    if(i<=10):
        print("%d*%2d=%2d"%(n,i,n*i))
        table(i+1)
table(1)'''

#factorial of a number using recursion
'''def fact(f):
    if(f==0):
        return 1
    else:
        f=f*fact(f-1)
    return f
print(fact(5))'''
