Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
t=()
print(type(t))
<class 'tuple'>
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3)
type(t)
<class 'tuple'>
t=(1,2,3,4,5)
print(t)
(1, 2, 3, 4, 5)
print(len(t))
5
t=(1,3,5,7,9)
t
(1, 3, 5, 7, 9)
t[2]
5
t[2]=10
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t[2]=10
TypeError: 'tuple' object does not support item assignment
>>> t=91,2,3,4,5,1,2)
SyntaxError: unmatched ')'
>>> t=(1,2,3,4,5,1,2)
>>> t
(1, 2, 3, 4, 5, 1, 2)
>>> t=(10,12.5,"Krishna")
>>> t
(10, 12.5, 'Krishna')
>>> a,b,c=t
>>> print(a)
10
>>> print(b)
12.5
>>> print(c)
Krishna
>>> print(a,b,c)
10 12.5 Krishna
>>> t=tuple(range(10,110,10))
>>> t
(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
>>> t[2:5]
(30, 40, 50)
>>> t[1:6]
(20, 30, 40, 50, 60)
>>> t[-1:-5]
()
>>> t[-2:-5:-1]
(90, 80, 70)
>>> t[::1]
(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
>>> t[::2]
(10, 30, 50, 70, 90)
>>> t[-2]
90
>>> t[2]
30
>>> t[3,2]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t[3,2]
TypeError: tuple indices must be integers or slices, not tuple
>>> t[3:2]
()
