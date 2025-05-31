Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=2
print(d)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> s=[1,2,3,4,5,6]
>>> s.remove(7)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.remove(7)
ValueError: list.remove(x): x not in list
>>> s[2]
3
>>> s[6]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s[6]
IndexError: list index out of range
>>> s="RaJu"
>>> s.swapcase()
'rAjU'
>>> s[2]
'J'
>>> s[5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[5]
IndexError: string index out of range
>>> d=['a':3,'b':5,'c':8]
SyntaxError: invalid syntax
>>> d=
SyntaxError: invalid syntax
>>> d={'a':3,'b':5,'c':8}
>>> d.'e'
SyntaxError: invalid syntax
>>> d['a']
3
>>> d['e']
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d['e']
KeyError: 'e'
>>> s=3+4j
>>> s.real
3.0
>>> s.real=3.5
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.real=3.5
AttributeError: readonly attribute
