'''#check the str is palindrome are not
s=input("enter a string:")
print("palindrome") if(s==s[::-1]) else print("not palindrome")'''

'''#check the str is symmetric palindrome are not
s=input("enter a string:")
m=len(s)//2
fh=s[:m]
sh=s[m:]
print("symmetric palindrome") if(fh==sh) else print("not symmetric palindrome")'''

'''#rotations
s=input("enter a string:")
p=int(input("enter no. of rotations:"))
c=''
c=s[-p:]+s[:-p]
print(c)'''

s=input("enter a string:")
p=int(input("enter no. of rotations:"))
c=s[p:]+s[:p]
print(c)

#input:rohith,r=3---->ithroh
#input:rohith,r=2---->throhi

