'''#Hierarichal inheritance
class Student:
    def __init__(self):
        self.name=input("Enter name:")
        self.rno=int(input("Enter rno:"))
        self.add=input("Enter address:")
    def stud_info(self):
        print(self.name,self.rno,self.add)
class MCA(Student):
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        super().__init__()
    def display(self):
        self.stud_info()
        print(self.s1,self.s2,self.s3)
class MBA(Student):
    def __init__(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        super().__init__()
    def display1(self):
        self.stud_info()
        print(self.s1,self.s2,self.s3)
m1=MCA("PYTHON","JAVA","DBMS")
m1.display()
m2=MBA("MS","IPR","MEFA")
m2.display1()

#single inheritance
class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a+self.b)
class child(parent):
    def display1(self):
        print(self.a-self.b)
a=int(input())
b=int(input())
c1=child(a,b)
c1.display()
c1.display1()

#multiple inheritance
class a:
    def m1(self):
        print("in m1 of x")
class b:
    def m2(self):
        print("in m2 of y")
class c(a,b):
    def m3(self):
        print("in m3")
c1=c()
c1.m1()
c1.m2()
c1.m3()

class a:
    def m1(self):
        print("in m1 of x")
class b:
    def m1(self):
        print("in m2 of y")
class c(a,b):
    def m3(self):
        print("in m3")
c1=c()
c1.m1()

class a:
    def m1(self):
        print("in m1 of x")
class b:
    def m1(self):
        print("in m1 of y")
class c(b,a):
    def m3(self):
        print("in m3")
c1=c()
c1.m1()

#Hybrid inheritance
class a:
    def m1(self):
        print("in m1")
class b(a):
    def m2(self):
        print("in m2")
class c(b):
    def m3(self):
        print("in m3")
class d(a):
    def m4(self):
        print("in m4")        
c1=c()
c1.m1()
c1.m2()
c1.m3()
d1=d()
d1.m1()
d1.m4()

#method overloading
class x:
    def m1(self):
        print("m1 with no para")
    def m1(self,a):
        print("m1 with one para")
    def m1(self,a,b):
        print("m1 with two para")
x1=x()
x1.m1(20,10)

class x:
    def m1(self):
        print("m1 with no para")
    def m1(self,b):
        print("m1 with two para")
    def m1(self,a):
        print("m1 with one para")
#always the last function is going to be executed so method overloading is partially supported in python
x1=x()
x1.m1(20)

class x:
    def op(self,i,*a):
        if(i=="int"):
            s=0
        else:
            s=''
        for p in a:
            s=s+p
        print(s)
x1=x()
x1.op("int",10,20,30)
x1.op("str","Varsha","Jayaram","(VJ)")

#method overriding
class x:
    def m1(self):
        print("in m1 of x")
    def m2(self):
        print("in m2 of x")
class y(x):
    def m1(self):
        print("in m1 of y")
        super().m1()
    def m3(self):
        print("in m3 of y")
class z(x):
    def m2(self):
        print("in m2 of z")
        super().m2()
    def m4(self):
        print("in m4 of z")
y1=y()
y1.m1()
y1.m2()
y1.m3()
z1=z()
z1.m1()
z1.m2()
z1.m4()

class x:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
x1=x("Python")
p=x1.__str__()
print(p)
x2=x("Java Script")
p=x2.__str__()
print(p)
x3=x("IOT")
p=x3.__str__()
print(p)

class student:
    def __init__(self,name,rno,add,marks):
        self.name=name
        self.rno=rno
        self.add=add
        self.marks=marks
    def __str__(self):
        return self.name+" "+str(self.rno)+" "+self.add+" "+str(self.marks)
x1=student("varsha",1606,"Rajam",2004)
print(x1)
x2=student("vJ",2210,"Rajam",2022)
print(x2)
x3=student("Jay",1302,"Rajam",199)
print(x3)

class student:
    def __init__(self,name,rno,add,marks):
        self.name=name
        self.rno=rno
        self.add=add
        self.marks=marks
    def __str__(self):
        return self.name+" "+str(self.rno)+" "+self.add+" "+str(self.marks)
x1=student("varsha",1606,"Rajam",2004)
print(x1)
x2=student("vJ",2210,"Rajam",2022)
print(x2)
x3=student("Jay",1302,"Rajam",1995)
print(x3)
x=[x1,x2,x3]
x.sort(key=lambda s:s.rno)
for student in x:
    print(student)'''
            



    


