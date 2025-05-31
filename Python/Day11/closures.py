'''def power(p):
    def pow(n):
        return p**n
    return pow
s=power(5)
r=s(3)
print(r)
s=power(4)
r1=s(3)
print(r1)
s=power(6)
r3=s(3)
print(r3)

#decorators
def dis(d):
    def new_display():
        print("**************")
        d()
        print("**************")
    return new_display
@dis
def display():
    print("Python programming")
display()

#zero division error
def division(d):
    def new_div(a,b):
        if b==0:
            return 0
        else:
            return d(a,b)
    return new_div
@division
def div(a,b):
    d=a/b
    return d
s=div(10,2)
print(s)
s=div(10,0)
print(s)'''


