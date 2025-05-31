#Bubble sort
'''def bubble_sort(l):
    for p in range(len(l)-1):
        for q in range(len(l)-1):
            if(l[q]>l[q+1]):
                l[q],l[q+1]=l[q+1],l[q]
        print(l)
    return l
l=list(map(int,input().split()))
print("Before sorting:",l)
b=bubble_sort(l)
print("After sorting:",b)

def bubble_sort(l):
    for p in range(len(l)-1):
        for q in range(len(l)-1):
            if(l[q]<l[q+1]):
                l[q],l[q+1]=l[q+1],l[q]
        print(l)
    return l
l=list(map(int,input().split()))
print("Before sorting:",l)
b=bubble_sort(l)
print("After sorting:",b)'''

'''def bubble_sort(l):
    for p in range(len(l)-1):
        for q in range(len(l)-1):
            if(len(l[q])>len(l[q+1])):
                l[q],l[q+1]=l[q+1],l[q]
        print(l)
    return l
l=list(map(str,input().split()))
print("Before sorting:",l)
b=bubble_sort(l)
print("After sorting:",b)

def bubble_sort(l):
    for p in range(len(l)-1):
        for q in range(len(l)-1):
            if(len(l[q])<len(l[q+1])):
                l[q],l[q+1]=l[q+1],l[q]
        print(l)
    return l
l=list(map(str,input().split()))
print("Before sorting:",l)
b=bubble_sort(l)
print("After sorting:",b)'''

#Selection sort
'''def sel_sort(l):
    for i in range(len(l)):
        mi=i
        for j in range(i+1,len(l)):
            if(l[j]<l[mi]):
                mi=j
        l[mi],l[i]=l[i],l[mi]
        print(l)
    return l
l=list(map(int,input().split()))
print("Before sorting:",l)
b=sel_sort(l)
print("After sorting:",b)'''

#Insertion sorrt
'''def insertion(l):
    for i in range(1,len(l)):
        temp=l[i]
        j=i-1
        while((j>=0)and(temp<l[j])):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=temp
        print(l)
    return l
l=list(map(int,input().split()))
print("Before sorting:",l)
b=insertion(l)
print("After sorting:",b)'''
