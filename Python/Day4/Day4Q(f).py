'''n=input("enter name of the student:")
r=int(input("enter roll number of the student:"))
s1,s2,s3=map(int,input("enter 3 subject marks of the student:").split())
print("Name of the student is:",n)
print("Roll number of the student is:",r)
print("Maths:",s1,"python:",s2,"Mt:",s3)
if((s1>=35) and (s2>=35) and (s3>=35)):
    total=s1+s2+s3
    avg=total/3
    if(avg>=75):
        print(n,"secured first class")
    elif(avg>=55):
        print(n,"secured second class")
    elif(avg>=35):
        print(n,"secured third class")
else:
    print(n,"is fail")'''


'''#switch
print("1.Add,2.Sub,3.Product,4.Division")
opt=int(input("enter your option:"))
a,b=map(int,input("enter a,b values:").split())
match(opt):
    case 1:print("Sum:",a+b)
    case 2:print("Difference:",a-b)
    case 3:print("Product:",a*b)
    case 4:print("Division:",a/b)
    case _:print("Invalid option, please try again")'''

'''#1---->square of n,2---->cube,3----->sqrt,4----->area of circle,5-------> area of rectangle
import math
print("1.Square,2.Cube,3.sqrt,4.area of circle,5.area of rectangle")
opt=int(input("enter your option:"))
n=int(input("enter value of n:"))
r=int(input("enter value of r:"))
l=int(input("enter value of l:"))
b=int(input("enter value of b:"))
match(opt):
    case 1:print("Square",n*n)
    case 2:print("Cube",n*n*n)
    case 3:print("sqrt",math.sqrt(n))
    case 4:print("area of circle",math.pi*r*r)
    case 5:print("area of rectangle",l*b)
    case _:print("Invalid option, please try again")


import math
print("1.Square,2.Cube,3.sqrt,4.area of circle,5.area of rectangle")
opt=int(input("enter your option:"))
match(opt):
    case 1:
           n=int(input("enter n:"))
           print("square:",n*n)
    case 2:
           n=int(input("enter n:"))
           print("cube:",n*n*n)
    case 3:
           n=int(input("enter n:"))
           s=math.sqrt(n)
           print("sqrt:",s)
    case 4:
           r=float(input("enter radius:"))
           area=math.pi*r*r
           print("area of circle%.2f"%(area))
    case 5:
           l,b=map(int,input("enter l,b values:").split())
           area=l*b
           print("area of rectangle",area)
    case _:print("Invalid option, please try again")'''
        




    
        
    
