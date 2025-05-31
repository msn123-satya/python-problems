'''#local variable
def m1():
    a=10
    b=20
    print(a,b)
def m2():
    c=30
    d=40
    print(c,d)
    #print(a)
m1()
m2()

def m1(a,b):
    print(a+b)
def m2(c,d):
    print(d-c)
m1(10,20)
m2(30,40)

#global variable
a=10
def m1():
    print(a)
m1()
a=a+20
m1()

a=10
def m1():
    global a
    print(a)
    a=a+10
    print(a)
m1()

#banking application
bal=100000
def Cust_info():
    Name=input("Enter your name:")
    Acc_num=int(input("Enter your account number:"))
    Address=input("Enter your address:")
    print(Name,Acc_num,Address)
def Check_bal():
    print("Current balance",bal)
def Deposit(amt):
    global bal
    bal=bal+amt
def Withdrawal(amt):
    global bal
    if(bal>amt):
        if(bal-amt>=2000):
            bal=bal-amt
        else:
            print("Maintain minimum balance")
    else:
        print("Insufficient funds")
print("*******************Banking Application********************")
while(True):
    print("1.Cust_info,2.Check_bal,3.Deposit,4.Withdrawal,5.Exit")
    opt=int(input("Enter your option:"))
    if(opt==1):
        Cust_info()
    elif(opt==2):
        Check_bal()
    elif(opt==3):
        amt=int(input("enter amount for deposit:"))
        Deposit(amt)
    elif(opt==4):
        amt=int(input("enter amount for withdrawal:"))
        Withdrawal(amt)
    elif(opt==5):
        break

#Student details
def St_info():
    Name=input("Enter your name:")
    s1,s2,s3=map(int,input("Enter 3 subject marks:").split())
    print("M3:",s1,"MT:",s2,"HT:",s3)
def Grade():
    s1,s2,s3=map(int,input("Enter 3 subject marks:").split())
    if((s1>=35) and (s2>=35) and (s3>=35)):
        print("Pass")
    else:
        print("fail")
print("*******************STUDENT DETAILS********************")
while(True):
    print("1.St_info,2.Grade,3.Exit")
    opt=int(input("Enter your option:"))
    if(opt==1):
        St_info()
    elif(opt==2):
        Grade()
    elif(opt==3):
        break'''


    
    
        

    
        
    
                
    
        
    
    
    
    
    
                  


