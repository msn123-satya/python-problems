# To print length of a list using recursion
'''def length(l):
    if l==[]:
        return 0
    else:
        return 1+length(l[1:])
l=list(map(int,input().split()))
print(length(l))'''

# To print sum of elements in a list using recursion
'''def sum(l):
    if l==[]:
        return 0
    else:
        return l[0]+sum(l[1:])
l=list(map(int,input().split()))
print(sum(l))'''

# To print max element iun a list
'''def max(l):
    l.sort()
    return l[-1]
l=list(map(int,input().split()))
print(max(l))'''

# To print min element in a list
'''def max(l):
    l.sort()
    return l[0]
l=list(map(int,input().split()))
print(max(l))'''
