#i/p:beads---->value for str1, leaps---->value for str2 o/p:aes(present in both strs)
'''str1=input()
str2=input()
set1=set(str1)
set2=set(str2)
p=set1.intersection(set2)
l=list(p)
l.sort()
print(''.join(l))'''

#i/p:        o/p:
#4            5 
#2 4 5 9      9
#4           11
#2 4 11 12   12
'''n1=int(input())
s1=set(map(int,input().split()))
n2=int(input())
s2=set(map(int,input().split()))
s=s1^s2
s3=list(s)
s3.sort() 
for p in s3:
    print(p)'''

