Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #the sum of 20 and 10 is 30
>>> a,b=20,10
>>> print("The sum of",a,"and",b,"is",a+b)
The sum of 20 and 10 is 30
>>> a,b=20,10
>>> print("The diff of",a,"and",b,"is",a-b)
The diff of 20 and 10 is 10
>>> #old style sum and diff
>>> a,b=20,10
>>> print("The sum of %d and %d is %d"%(a,b,a+b))
The sum of 20 and 10 is 30
>>> print("The diff of %d and %d is %d"%(a,b,a-b))
The diff of 20 and 10 is 10
>>> r=2.3467
>>> print("%f"%r)
2.346700
>>> print("%.2f"%r)
2.35
>>> r="lokesh"
>>> print("Name=%s"%r)
Name=lokesh
>>> r="lokesh"
>>> print("IT & Educational minister of AP is %s"%r)
IT & Educational minister of AP is lokesh
>>> a=35
>>> print("%o,%x"%(a,a))
43,23
>>> #20+10=30
>>> a,b=20,10
... print("%d+%d=%d"%(a,b,a+b))
SyntaxError: multiple statements found while compiling a single statement
>>> a,b=20,10
>>> print("%d+%d=%d"%(a,b,+b))
20+10=10
>>> print("%d+%d=%d"%(a,b,a-b))
20+10=10
>>> print("%d-%d=%d"%(a,b,a-b))
20-10=10
>>> print("%d*%d=%d"%(a,b,a*b))
20*10=200
>>> print("%d+%d=%d"%(a,b,a+b))
20+10=30
