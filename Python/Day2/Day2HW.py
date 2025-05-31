a=[1,2,3,4,5]
p=2
c=a[-p:]+a[:-p]
print(c)

s=input("enter a string:")
p=int(input("enter no. of rotations:"))
c=s[-p:]+s[:-p]
print(c) 
