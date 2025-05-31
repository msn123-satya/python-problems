#unique character #asfddagha
'''s=input()
c=0
for p in s:
    if(s.count(p)==1):
        c=c+1
print(c)'''

#i/p:gasg!g54@#vscdls* o/p:4(!,@,#,*)
'''s=input()
c=0
for p in ("!,#,*,@"):
    if(s.count(p)==1):
        c=c+1
print(c)
#or
s=input()
c=0
for p in s:
    if(p.isalpha() or p.isdigit()):
        continue
    else:
        c=c+1
print(c)'''



#i/p:OqPputLE o/p:2 (for the given str , there are only two consonants that come after vowel is q and t)
'''s=input()
c=0
v="aeiouAEIOU"
for p in range(0,len(s)-1):
    if(s[p] in v):
        if(s[p+1].isalpha()) and (s[p+1] not in v):
            c=c+1
print(c)'''

#i/p:aabbcde (original str:aabbcde original str len:7,compressed str:a2b2c1d1e1 and compressed str len:10)
#10>7 so o/p:NO
'''s=input()
s1=set(s)
s2=list(s1)
s2.sort()
c=""
for p in s2:
    d=s.count(p)
    c=c+p+str(d)
print(c)
if(len(s)>len(c)):
    print("Yes")
else:
    print("No")'''

#balanced string
#i/p:5               #o/p: 3
#aabaaba
#bbaabb
#abbab
#aaabb
#abbbbabbb
def bal_str(s):
    if(len(s)%2!=0):
        m=len(s)//2
        mc=s[m]
        fh=s[:m]
        sh=s[m+1:]
        f1=fh.count(mc)
        s1=sh.count(mc)
        if((f1==s1) and (f1>=0)):
            return 1
    return 0        
n=int(input())
l=[]
for p in range(n):
    s=input()
    l.append(s)
print(l)
c=0
for p in l:
    c=c+bal_str(p)
print(c)
    
    
    


