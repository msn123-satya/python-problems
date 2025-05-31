#the num is automorphic number
'''def auto_num(num):
    s=num**2
    m=10**len(str(num))
    if s%m==num:
        return True
    else:
        return False
n=int(input())
if auto_num(n):
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")'''

n=int(input())
s=str(n)
l=len(s)
p=n**2
d=p%(10**l)
if n==d:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")
    

