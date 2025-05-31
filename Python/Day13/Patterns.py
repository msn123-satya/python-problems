'''#patterns
#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5
n=int(input())
i=1
while(i<=n):
    j=n
    while(j>=i):
        print(j,end=" ")
        j=j-1
    print()
    i=i+1

#A
#A B
#A B c
#A B C D
#A B C D E
n=int(input())
i=1
while(i<=n):
    j=1
    k=ord('A')
    while(j<=i):
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1

#A B C D E
#A B C D
#A B C
#A B
#A 
n=int(input())
i=n
while(i>=1):
    j=1
    k=ord('A')
    while(j<=i):
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i-1

#E
#E D
#E D C
#E D C B
#E D C B A
n=int(input())
i=n
while(i>=1):
    j=n
    k=ord('E')
    while(j>=i):
        print(chr(k),end=" ")
        j=j-1
        k=k-1
    print()
    i=i-1

#1 
#2  3 
#4  5   6 
#7  8   9 10 
#11 12 13 14 15
n=int(input())
i=1
k=1
while(i<=n):
    j=1
    while(j<=i):
        print(k,end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1

#A 
#B C 
#D E F 
#G H I J 
#K L M N O 
n=int(input())
i=1
k=ord('A')
while(i<=n):
    j=1
    while(j<=i):
        print(chr(k),end=" ")
        j=j+1
        k=k+1
    print()
    i=i+1

#1
#1 *
#1 * 3
#1 * 3 *
#1 * 3 * 5
n=int(input())
i=1
while(i<=n):
    j=1
    while(j<=i):
        if (j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
        j=j+1
    print()
    i=i+1

l=['abc','ABC','def','GHY','hij','XYZ','var','jay']
r=list(filter(lambda x:x.islower(),l))
print(r)

l=['Varsha Jay','varsha jai','Jai Ram','Prabhas Raju']
r=list(filter(lambda x:x.istitle(),l))
print(r)

l=['abc','def','hij','var','jay']
r=tuple(map(lambda x:x.upper(),l))
print(r)'''

l=['varsha jai','jai ram','prabhas raju']
r=list(map(lambda x:x.title(),l))
print(r)
       

