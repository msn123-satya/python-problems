#fabinocci series using recursion
'''def fib(n):
    if n<=1:
        return n
    else:
        d=fib(n-1)+fib(n-2)
    return d
print(fib(6))'''

#checking whether given str is palindrome or not using recursion
'''def pal(s):
    if len(s)<=0:
        return True
    else:
        if(s[0]==s[-1]):
            return pal(s[1:-1])
        else:
            return False
s=pal("liril")
print(s)
s1=pal("varsha")
print(s1)'''

#finding no.of vowels in a given str using recursion
'''def c_v(s):
    if len(s)==0:
        return 0
    elif(s[0] in "aeiou"):
        return 1+c_v(s[1:])
    else:
        return c_v(s[1:])
print(c_v("liril"))'''
    
#finding no.of consonants in a given str using recursion      
'''def c_v(s):
    if len(s)==0:
        return 0
    elif(s[0] not in "aeiou"):
        return 1+c_v(s[1:])
    else:
        return c_v(s[1:])
print(c_v("liril"))'''

#finding length of a str using recursion
'''def count(s):
    if(s==''):
        return 0
    else:
        return 1+count(s[1:])
print(count("HaRe KrIshNa"))'''

#_____________HACKERRANK______________
#lists
'''i=1
l=[]
n=int(input())
while(i<=n):
    cmd=input()
    s=cmd.split()
    if(s[0]=="insert"):
        a,b=int(s[1]),int(s[2])
        l.insert(a,b)
    elif(s[0]=="remove"):
        a=int(s[1])
        l.remove(a)
    elif(s[0]=="append"):
        a=int(s[1])
        l.append(a)
    elif(s[0]=="sort"):
        l.sort()
    elif(s[0]=="pop"):
        l.pop()
    elif(s[0]=="reverse"):
        l.reverse()
    elif(s[0]=="print"):
        print(l)
    i=i+1'''

#max
'''n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
m1=max(l)
c=l.count(m1)
s=l[-(c+1)]
print(s)'''

#min
'''n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
m1=min(l)
c=l.count(m1)
s=l[c]
print(s)'''

#sorting the numbers and words based on numerics and alphabets order
'''s=["lokesh",5,2,"naga raju","sachin","cbn",3,1,9,"pspk",12,8,"jagan",11,"gorantla madav","avanthiganta","rambabusaroja","kasaireddy"]
print(s)
ln=[]
ls=[]
for p in s:
    if(type(p)==int):
        ln.append(p)
    else:
        ls.append(p)
ln.sort()
ls.sort()
l=ln+ls
print(l)'''

#l=[1,2,3,4,5,1,2,6,3]
#l=[1,2,3,4,5,6]
'''l=list(map(int,input().split()))
print(l)
r=[]
for p in l:
    if p not in r:
        r.append(p)
print(r)'''

#2 numbers in fabinocci series (0 1 1 2 3 5 8 13 21 34 55 89)
#less than 10---->even numbers---->[2,8]----->10(sum)
#less than 100------>even numbers------>[2,8,34]------>44(sum)
'''def even_fib(n):
    s1=0
    a,b=1,2
    while(a<=n):
        if(a%2==0):
            s1=s1+a
        a,b=b,a+b
    return s1
n=int(input())
for p in range(n):
    n=int(input())
    res=even_fib(n)
    print(res)'''
            
#seperating even and odd in a phone num
'''n=int(input())
l=list(map(int,str(n)))
print(l)
el=[]
ol=[]
for p in l:
    if(p%2==0):
        el.append(p)
    else:
        ol.append(p)
print(el)
print(ol)
ol.sort()
el.reverse()
d=ol+el
print(d)
for p in d:
    print(p,end="")'''
            
        






    
