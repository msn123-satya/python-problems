Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string
s='c'
s
'c'
type(s)
<class 'str'>
s='abc'
type(s)
<class 'str'>
s="VJ"
type(s)
<class 'str'>
s='''Varsha
jaya
... Ram'''
>>> print(s)
Varsha
jaya
Ram
>>> type(s)
<class 'str'>
>>> s='varsha chem'
>>> print(s)
varsha chem
>>> len(s)
11
>>> s=varsha
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s=varsha
NameError: name 'varsha' is not defined. Did you mean: 'vars'?
>>> s='Varsha'
>>> r='Jaya ram'
>>> s+r
'VarshaJaya ram'
>>> s+" "+r
'Varsha Jaya ram'
>>> x=123
>>> y=456z='567'
SyntaxError: invalid decimal literal
>>> y=456
>>> z="567"
>>> x+y
579
>>> y+z
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    y+z
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> y+int(z)
1023
>>> s+x
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s+x
TypeError: can only concatenate str (not "int") to str
>>> s+str(x)
'Varsha123'
>>> x+y+int(z)
1146
