'''from abc import*
class RBI(ABC):  
    def min_bal(self):#Abstract method
        pass
    def RI(self):#Non-Abstract method
        print("RI is 6.5%")
class SBI(RBI):
    def min_bal(self):
         print("Min balace is 2000 rupees")
class HDFC(RBI):
    def min_bal(self):
         print("Min balace is 0 rupees")
class ICICI(RBI):
    def min_bal(self):
         print("Min balace is 2000 rupees")
s1=SBI()
s1.min_bal()
s1.RI()
h1=HDFC()
h1.min_bal()
h1.RI()
i1=ICICI()
i1.min_bal()
i1.RI()

from abc import*
class RBI(ABC):
    def min_bal(self):#Abstract method
        pass
    def RI(self):#Non-Abstract method
        print("RI is 6.5%")
class SBI(RBI):
    def min_bal(self):
         print("Min balace is 2000 rupees")
class HDFC(RBI):
    def min_bal(self):
         print("Min balace is 0 rupees")
class ICICI(RBI):
    def min_bal(self):
         print("Min balace is 2000 rupees")
s=input("Enter classname:")
classname=globals()[s]
c1=classname()
c1.min_bal()
c1.RI()

from abc import*
class Operation(ABC):
    def op(self):
        pass
class Add(Operation):
    def op(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
class Sq(Operation):
    def op(self,a):
        self.a=a
        print(self.a*self.a)
class Cube(Operation):
    def op(self,a):
        self.a=a
        print(self.a*self.a*self.a)
a1=Add()
a1.op(10,5)
s1=Sq()
s1.op(5)
c1=Cube()
c1.op(6)'''

from abc import*
class Vehicles(ABC):
    def wheels(self):
        pass
class Car(Vehicles):
    def wheels(self):
         print("Car contains 4 wheels")
class Bus(Vehicles):
    def wheels(self):
         print("Bus contains 6 wheels")
class Auto(Vehicles):
    def wheels(self):
         print("Auto contains 3 wheels")
s=input("Enter classname:")
classname=globals()[s]
c1=classname()
c1.wheels()

            
