Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=[1,2,3,4,5]
print(s)
[1, 2, 3, 4, 5]
>>> id(s)
2319132544512
>>> y=s.copy()
>>> y
[1, 2, 3, 4, 5]
>>> id(y)
2319132544064
>>> y[2]=6
>>> y
[1, 2, 6, 4, 5]
>>> s
[1, 2, 3, 4, 5]
>>> 
>>> #shallow copy
>>> s=[1,2,3,4,5]
>>> s
[1, 2, 3, 4, 5]
>>> id(s)
2319127024960
>>> y=s
>>> y
[1, 2, 3, 4, 5]
>>> id(y)
2319127024960
>>> id(s)
2319127024960
>>> y[3]=6
>>> y
[1, 2, 3, 6, 5]
>>> s
[1, 2, 3, 6, 5]
>>> 
>>> #str updation
>>> s="Varsha"
>>> r=list(s)
>>> r
['V', 'a', 'r', 's', 'h', 'a']
>>> "".join(r)
'Varsha'
>>> s="varsha"
>>> r=list(s)
>>> r[2]='h'
>>> r
['v', 'a', 'h', 's', 'h', 'a']
>>> "".join(r)
'vahsha'
