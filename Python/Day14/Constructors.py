'''#arithmetic operations using non-static variable
class Test:
    def __init__(self):
        self.a=int(input("Enter a:"))
        self.b=int(input("Enter b:"))
        print(self.a,self.b)
    def add(self):
        print("Addition",self.a+self.b)
    def sub(self):
         print("subtraction",self.a-self.b)
    def mul(self):
         print("Multiplication",self.a*self.b)
    def div(self):
         print("Division",self.a/self.b)
t1=Test()
t1.add()
t1.sub()
t1.mul()
t1.div()

class student():
    cname="GMRIT"
    def __init__(self,name,rno,address,s1,s2,s3):
        self.name=name
        self.rno=rno
        self.address=address
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def student_info(self):
        print("College name:",student.cname)
        print("Name",self.name)
        print("Roll number",self.rno)
        print("Address",self.address)
        print("MT",self.s1,"HT",self.s2,"TP",self.s3)
    def find_result(self):
        if ((self.s1>40) and (self.s2>40) and (self.s3>.40)):
            total=self.s1+self.s2+self.s3
            avg=total/3
            if (avg>80):
                print(self.name,"secured first class")
            elif (avg>60):
                print(self.name,"secured second class")
            elif (avg>40):
                print(self.name,"secured third class")
        else:
            print(self.name,"is fail")
n=int(input("enter no.of students:"))
i=1
while(i<=n):
    print("**************************")
    name=input("Enter name:")
    rno=int(input("Enter Roll number:"))
    address=input("Enter Address:")
    s1,s2,s3=map(int,input("Enter 3 sub marks:").split())
    st=student(name,rno,address,s1,s2,s3)
    st.student_info()
    st.find_result()
    print("**************************")
    i=i+1

class book():
    lname="GMRIT"
    def __init__(self,name,aname,pages,cost):
        self.name=name
        self.aname=aname
        self.pages=pages
        self.cost=cost
    def info(self):
        print("Library name",book.lname)
        print("Book name",self.name)
        print("Author name",self.aname)
        print("No.of pages",self.pages)
        print("Cost of the book",self.cost)
n=int(input("Enter no.of books:"))
i=1
while(i<=n):
    print("**************************")
    name=input("Enter book name:")
    aname=input("Enter author name:")
    pages=int(input("Enter no.of pages:"))
    cost=int(input("Enter cost:"))
    print("**************************")
    i=i+1

#has a relation
class x:
    a=1000
    def m1(self):
        self.b=2000
    def m2(self):
        print("in m2")
    def add(a,b):
        print("sum:",a+b)
class y:
    c=3000
    def __init__(self):
        self.d=4000
    def m3(self):
        print("in m3")
    def display(self):
        print(y.c)
        print(self.d)
        self.m3()
        x.add(10,5)
        x1=x()
        print(x1.a)
        x1.m1()
        print(x1.b)
        x1.m2()
y1=y()
y1.display()

class student:
    def __init__(self,name,rno,marks):
        self.name=name
        self.rno=rno
        self.marks=marks
    def student_info(self):
        print(self.name,self.rno,self.marks)
class faculty:
    def update(s1):
        s1.marks=96
        s1.student_info()
s1=student("Jay",478,86)
s1.student_info()
faculty.update(s1)

#employee #management----->salary of employee
class employee:
    def __init__(self,name,idno,salary):
        self.name=name
        self.idno=idno
        self.salary=salary
    def employee_info(self):
        print(self.name,self.idno,self.salary) 
class management:
    def update(e1):
        e1.salary=96000
        e1.employee_info()
e1=employee("Jay",80354,70000)
e1.employee_info()
management.update(e1)'''

import math
class Test:
    a=10
    b=20
    def add(self):
        print("Addition:",Test.a+Test.b)
    def diff():
        print("Difference:",Test.a-Test.b)
    def mul(m1,m2):
        print("Product:",m1*m2)
    def factorial():
        d=math.factorial(Test.a)
        print(d)
    @classmethod
    def sqrt(cls):
        e=int(input("enter value:"))
        s=math.sqrt(e)
        print(s)
t1=Test()
t1.add()
Test.diff()
Test.mul(10,5)
Test.factorial()
Test.sqrt()
        


        


    
    

    
    
        
        
