#area of rectangle
class Rectangle:
    def insert(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        a=(self.l*self.b)
        print("%.2f"%a)
c1=Rectangle()
l=int(input())
b=int(input())
c1.insert(l,b)
c1.area()

#area of Triangle
class Triangle:
    def insert(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        a=((1/2)*self.l*self.b)
        print("%.2f"%a)
c1=Triangle()
l=int(input())
b=int(input())
c1.insert(l,b)
c1.area()
