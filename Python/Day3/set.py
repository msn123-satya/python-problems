Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={}
>>> type(s)
<class 'dict'>
>>> s={10}
>>> type(s)
<class 'set'>
>>> s={'a':10}
>>> type(s)
<class 'dict'>
>>> s=set{}
SyntaxError: invalid syntax
>>> s=set()
>>> type(s)
<class 'set'>
>>> s=set(range(1,11,1))
>>> print(s)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> s={10,20,30,40,50}
>>> s
{50, 20, 40, 10, 30}
>>> s={1,2,3,4,5,1,2}
>>> s
{1, 2, 3, 4, 5}
>>> s={12,23,24,26}
>>> s
{24, 26, 12, 23}
>>> s.add(20)
>>> s
{12, 20, 23, 24, 26}
>>> id(s)
1873168943808
>>> s={12,23,24,26}
>>> id{s}
SyntaxError: invalid syntax
>>> id(s)
1873168952096
>>> s.add(20)
>>> s
{12, 20, 23, 24, 26}
>>> id(s)
1873168952096
>>> s={10,12,"vj","krishna",2+3j}
>>> s
{'vj', 'krishna', 10, (2+3j), 12}
