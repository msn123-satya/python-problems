'''#static variable within a class
class Test:
    a=2000
    b=3000
    def display(self):
        print(Test.a,Test.b)
    def update(self):
        Test.a=Test.a+100
        Test.b=Test.b+200
t1=Test()
t1.display()
t1.update()
t1.display()
t2=Test()
t2.display()
t2.update()
t2.display()

#static & non-static variable within a class
class Test:
    a=2000
    def insert(self):
        self.b=3000
    def display(self):
        print(Test.a,self.b)
    def update(self):
        Test.a=Test.a+100
        self.b=self.b+200
t1=Test()
t1.insert()
t1.display()
t1.update()
t1.display()
t2=Test()
t2.insert()
t2.display()
t2.update()
t2.display()

#static & non-static variable outside of a class
class Test:
    a=2000
    def insert(self):
        self.b=3000
    def display(self):
        print(Test.a,self.b)
t1=Test()
t1.insert()
print(t1.a,t1.b)
print(Test.a)'''

class Circle:
    pi=3.14
    def insert(self,r):
        self.r=r
    def area(self):
        a=(Circle.pi*self.r*self.r)
        print("%.2f"%a)
    def perimeter(self):
        p=(2*Circle.pi*self.r)
        print("%.2f"%p)
c1=Circle()
r=int(input())
c1.insert(r)
c1.area()
c1.perimeter()

        
        
