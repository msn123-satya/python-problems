class workerdetail:
    def __init__(self,name,ecode,sal):
        self.name=name
        self.ecode=ecode
        self.sal=sal
    def display(self):
        print(self.name,self.ecode,self.sal)
    def HRA(self):
        return 0.6*self.sal
class officersal(workerdetail):
    def DA(self):
        return 0.98*self.sal
class managersal(officersal):
    def CA(self):
        return 0.2*self.sal
ecode=int(input("Enter employee code:"))
name=input("Enter name:")
sal=int(input("Enter Basic salary:"))
m1=managersal(name,ecode,sal)
m1.display()
H=m1.HRA()
D=m1.DA()
C=m1.CA()
print("HRA is",H)
print("DA is",D)
print("CA is",C)
