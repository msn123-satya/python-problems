#merge sort
'''def merge(left,right):
    m=[]
    i=0
    j=0
    while ((i<len(left)) and (j<len(right))):
        if(left[i]<right[j]):
            m.append(left[i])
            i=i+1
        else:
            m.append(right[j])
            j=j+1
    m=m+left[i:]+right[j:]
    return m
def merge_sort(l):
    m=len(l)//2
    if(len(l)==1):
        return l
    left=merge_sort(l[:m])
    right=merge_sort(l[m:])
    d=merge(left,right)
    return d
l=[40,60,30,50,10,20]
print("Before sorting:",l)
m=merge_sort(l)
print("After sorting:",m)'''

#run-time error
'''print("begin")
a=int(input())
b=int(input())
c=a/b
print(c)
print("end")'''

#exception handling for run-time error
'''print("begin")
a=int(input())
try:
    b=int(input())
    c=a/b
    print(c)
except(ZeroDivisionError):
    print("second num can't be zero")
print("end")'''

#one try with multiple except block
'''print("begin")
a=int(input())
try:
    b=int(input())
    c=a/b
    print(c)
except(ValueError):
    print("second num should be int")
except(ZeroDivisionError):
    print("second num can't be zero")
print("end")'''

#global error
'''a=10
def m1():
    #global a
    print(a)
    a=a+10
    print(a)
m1()'''

#assertion error
'''def eligible_vote(age):
    assert(age>=18),"age should be greater than 18"
    print("Eligible for vote")
eligible_vote(23)
eligible_vote(15)'''

#exception handling for assertion error
def eligible_vote(age):
    assert(age>=18),"age should be greater than 18"
    print("Eligible for vote")
try:
    eligible_vote(23)
    eligible_vote(15)
except(AssertionError):
    print("age should be greater than 18")
    


