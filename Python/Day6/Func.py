'''#function without arguement,without Returntype
def add():
    a=10
    b=5
    print("sum:",a+b)
add()

#function with arg,without Rt
def even_odd(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
n=int(input("enter n:"))
even_odd(n)

#12345---->input
#1925----->output
#if odd num square it,if even num ignore it
def otp(s):
    l=[int(p) for p in s]#list comprahention
    r=[]
    for p in l:
        if(p%2!=0):
            d=p*p
            r.append(d)
    for p in r:
        print(p,end='')
s=input("enter a str:")
otp(s)

#func with arg and with rt
def add(a,b):
    s=a+b
    return s
a,b=map(int,input().split())
s=add(a,b)
print("sum",s)

#weights
def weight(p):
    w=10**(ord(p)-ord('A'))
    return w
s=input()
s=s.upper()
c=0
for p in s:
    w=weight(p)
    c=c+w
print(c)

#---->descending order
def number(n):
    l=list(map(int,str(n)))
    l.sort(reverse=True)
    r=list(map(str,l))
    s=''.join(r)
    return s
n=int(input())
s=number(n)
print(s)

#---->ascending order with 0 in second position
def number(n):
    l=list(map(int,str(n)))
    l.sort()
    if(l[0]==0):
        l[0],l[1]=l[1],l[0]
    r=list(map(str,l))
    s=''.join(r)
    return s
n=int(input())
s=number(n)
print(s)''' 





    

