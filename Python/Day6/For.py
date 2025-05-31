'''#palindrome
n=input("enter a str:")
r=''
for p in range(len(s)-1,-1,-1):
    r=r+s[p]
if(r==s):
    print("palindrome")
else:
    print("Not palindrome")

#the boy ran----->input
#nar yob eht----->output
s=input("enter a str:")
r=s.split()
for p in range(len(r)-1,-1,-1):
    if(p!=0):
        d=r[p][::-1]
        print(d,end=" ")
    else:
        d=r[p][:-1]
        print(d)'''



