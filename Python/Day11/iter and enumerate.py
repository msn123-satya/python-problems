Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5]
>>> r=iter(l)
>>> next(r)
1
>>> next(r)
2
>>> next(r)
3
>>> next(r)
4
>>> next(r)
5
>>> l=[2,4,6,8,10]
>>> r=iter(l)
>>> for p in r:
...     print(p)
... 
...     
2
4
6
8
10
>>> l=[1,2,3,4,5]
>>> r=enumerate(l)
>>> next(r)
(0, 1)
>>> next(r)
(1, 2)
>>> next(r)
(2, 3)
>>> next(r)
(3, 4)
>>> next(r)
(4, 5)
>>> next(r)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    next(r)
StopIteration
>>> l=[10,20,30,40,50]
>>> r=enumerate(l,5)
>>> next(r)
(5, 10)
>>> next(r)
(6, 20)
next(r)
(7, 30)
next(r)
(8, 40)
next(r)
(9, 50)
