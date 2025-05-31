'''#single inheritance
class person:
    def insert(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(self.name,self.address)
class faculty(person):
    def __init__(self,id1,sub,salary):
        self.id1=id1
        self.sub=sub
        self.salary=salary
        self.insert("Varsha","Rajam")
    def fac_info(self):
        self.display()
        print(self.id1,self.sub,self.salary)
f1=faculty(123,"MT",100000)
f1.fac_info()

class x:
    a=100
    def __init__(self,b):
        self.b=b
    def m1(self):
        print("in m1")
class y(x):
    c=300
    def __init__(self,d):
        self.d=d
        super().__init__(2000)
    def m2(self):
        print("in m2")
    def display(self):
        print(y.c)
        print(self.d)
        print(self.b)
        self.m2()
        print(y.a,x.a)
        self.m1()
y1=y(400)
y1.display()

#multilevel inheritance
class person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
class faculty(person):
    def __init__(self,name,address,id1,sub):
        self.id1=id1
        self.sub=sub
        super().__init__(name,address)
class semployee(faculty):
    def __init__(self,name,address,id1,sub,salary):
        self.salary=salary
        super().__init__(name,address,id1,sub)
    def fac_info(self):
        print(self.name,self.address,self.id1,self.sub,self.salary)
s1=semployee("krishna","Hyd",123,"python",60000)
s1.fac_info()'''

class person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
class employee(person):
    def __init__(self,id1,sub):
        self.id1=id1
        self.sub=sub
        super().__init__("Jay","Hyd")
class semployee(employee):
    def __init__(self,salary):
        self.salary=salary
        super().__init__(102,"MED")
    def emp_info(self):
        print(self.name,self.address,self.id1,self.sub,self.salary)
s1=semployee(60000)
s1.emp_info()
        
        
