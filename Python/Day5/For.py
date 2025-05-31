Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s="VARSHA"
for p in s:
    print(p)

V
A
R
S
H
A
>>> s="VARSHA"
>>> for p in s:
...     print(p,end=" ")
... 
V A R S H A 
>>> s=[123,26,99]
>>> for p in s:
...     print(p,end=" ")
... 
123 26 99 
>>> for p in range(1,11,1)
SyntaxError: expected ':'
>>> for p in range(1,11,1):
...     print(p,end=" ")
... 
...     
1 2 3 4 5 6 7 8 9 10 
>>> for p in range(10,55,5):
...     print(p,end=" ")
... 
...     
10 15 20 25 30 35 40 45 50 
>>> for p in range(30,61,2):
...     print(p,end=" ")
... 
...     
30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 
>>> for p in range(61,29,-2):
...     print(p,end=" ")
... 
...     
61 59 57 55 53 51 49 47 45 43 41 39 37 35 33 31 
>>> for p in range(2,11,2):
...     print(p,end=" ")
... 
...     
2 4 6 8 10 
>>> for p in range(1,10,2):
...     print(p,end=" ")
... 
...     
1 3 5 7 9 
