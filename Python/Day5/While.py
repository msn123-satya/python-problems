'''#while
#1-5
i=1
while(i<=5):
    print(i)
    i=i+1

#5-1
i=5
while(i>=1):
    print(i)
    i=i-1

#2 4 6 8 10
i=2
while(i<=10):
    print(i)
    i=i+2

#1 3 5 7 9
i=1
while(i<=9):
    print(i)
    i=i+2

#sum of 10 numbers
i=1
s=0
while(i<=10):
    s=s+i
    i=i+1
print("sum:",s)

#even and odd sum of 1-20
es=0
os=0
i=1
while(i<=20):
    if(i%2==0):
        es=es+i
    else:
        os=os+i
    i=i+1
print("even sum:",es)
print("odd sum:",os)

#sum of digits
n=int(input("enter a number:"))
s=0
while(n!=0):
    r=n%10
    s=s+r
    n=n//10
print("sum of digits:",s)

#find reverse of a number and check whether palindrome or not
n=int(input("enter a number:"))
s=0
m=n
while(n!=0):
    r=n%10
    s=(s*10)+r
    n=n//10
print("reverse of the number",s)
if(m==s):
    print(m,"is palindrome")
else:
    print(m,"is not palindrome")

#num is prime or not
n=int(input("enter a number:"))
c=0
i=1
while(i<=n):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")

#perfect num or not
n=int(input())
c=0
i=1
while(i<=(n//2)):
    if(n%i==0):
        c=c+i
    i=i+1
if(n==c):
    print("YES")
else:
    print("NO")

#fabanocci series
n=int(input())
i=0
j=1
print(i,j,end=" ")
c=3
k=i+j
while(c<=n):
    print(k,end=" ")
    i=j
    j=k
    k=i+j
    c=c+1

#armstrong number or not
n=int(input())
s=0
m=n
while(n!=0):
    r=n%10
    s=s+(r*r*r)
    n=n//10
if(m==s):
    print("YES")
else:
    print("NO")'''
    


    

    





        

        
    

    
