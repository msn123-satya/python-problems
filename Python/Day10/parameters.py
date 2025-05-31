'''#Default parameters
def add(a=10,b=7):
    print(a+b)
add()
add(15)
add(15,10)

#Non-Default parameters
def add(a,b):
    print(a+b)
add(12,5)
add(4.5,5)
add("varsha","jay")

#Orbitary parameters for single star
def add(*a,b):
    print(a,b)
    print(type(a))
    print(sum(a)+b)
add(10,20,30,40)#error

def add(*a,b=50):
    print(a,b)
    print(type(a))
    print(sum(a)+b)
add(10,20,30,40)

def add(b,*a):
    print(a,b)
    print(type(a))
    print(sum(a)+b)
add(10,20,30,40)

#Orbitary parameters for multistar star
def info(**a):
    print(a)
    print(type(a))
info(a=10,b=20,c=30)
info(name="Varsha",rollnum=803,dept="Chem",sub="MT")

#keyword,non-keyword paramter/argument
def work(name,project):
    print(name,"is working in",project,"project")
work("Radha","Fire fighiting robot")#Non-Keyword argument
work(project="Bus ticketing system",name="Krishna")#keyword argument

#lambda function
s=lambda a,b:a+b
p=s(20,10)
print(p)

#syntax: lambda var1,var2,var3,.....,varn:expression

#mul
s=lambda a,b:a*b
p=s(10,5)
print(p)

#list passing to lambda
s=lambda n:n%2==0
l=[1,2,3,4,5,6]
r=[p for p in l if(s(p))]
print(r)

#squares to the list
s= lambda x:x*x
l=[1,2,3,4,5,6]
r=[s(p) for p in l]
print(r)

#cubes to the list
s= lambda x:x*x*x
l=[1,2,3,4,5,6]
r=[s(p) for p in l]
print(r)

#from the list l=[2,-3,-4,8,-10] saggregate +ve number
s=lambda n:n>=0
l=[2,-3,-4,8,-10]
r=[p for p in l if(s(p))]
print(r)

#without list comp
l=[]
for p in range(1,11):
    l.append(p)
print(l)

#with list comp
#[outer_var for loop[cond]]
l=[p for p in range(1,11)]
print(l)

#1-20 even number squares
l=[]
for p in range(1,21):
    if(p%2==0):
        d=p*p
        l.append(d)
print(l)

#with list comp
l=[p*p for p in range(1,21) if (p%2==0)]
print(l)

#30-50 odd number cubes
l=[]
for p in range(30,51):
    if(p%2!=0):
        d=p*p*p
        l.append(d)
print(l)

#with list comp
l=[p*p*p for p in range(30,51) if (p%2!=0)]
print(l)'''





        
        






