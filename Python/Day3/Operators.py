Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#+,-,*,/,//,%,**
a=10
b=4
a+b
14
a-b
6
a*b
40
a/b
2.5
a//b
2
a%b
2
a**b
10000
a**2
100
b**3
64
5+True-2+3j+6j+19
(23+9j)
4*3+4*3
24
2+3*2+4
12
2+3*2+3
11
(2+3)*(2+3)
25
3+2*4+5/2+5//2
15.5
#relational operators
a=10
b=6
a>b
True
a<b
False
a>=b
True
a<=b
False
a==b
False
a!=b
True
'a'>'A'
True
'a','f'
('a', 'f')
'a'<'f'
True
'f'>'d'
True
ord('a')
97
ord('z')
122
ord('A')
65
char(97)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    char(97)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(97)
'a'
chr(111)
'o'
chr(99)
'c'
'abc'>'abd'
False
#logical---->and,or,not
((5>2)and(2>1))
True
((4!=2)and(5>2))
True
((4!=4)and(5>2))
False
(4>1)or(6>7)
True
not(5>2)
False
not(2<3)
False
not(4<3)
True
100 or 200 or 300
100
100 and 200 and 300
300
100 and 200 or 300
200
100 and 200 and false
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    100 and 200 and false
NameError: name 'false' is not defined. Did you mean: 'False'?
100 and 200 and False
False
#membership operators.....>in,not in
s="Jayaram"
"k" in s
False
"J" in s
True
"k" not in s
True
"j" not in s
True
"J" in s
True
"J" not in s
False
"V" not in s
True
p=["TDP","JSP","BJP"]
"TDP" in p
True
"YSRCP" not in p
True
"YSRCP" in p
False
"lokesh" not in p
True
5 not in [1,2,3,4,6]
True
's' in 'swathi'
True
#identity operators.....>is,is not
a=10
id(a)
140724568390360
a=a+10
id(a)
140724568390680
a=10
b=10
a==b
True
a!=b
False
a is b
True
a is not b
False
a=10
>>> b=20
>>> a==b
False
>>> a!=b
True
>>> a is b
False
>>> a is not b
True
>>> a=10
>>> b=10
>>> id(a),id(b)
(140724568390360, 140724568390360)
>>> a==b
True
>>> a!=b
False
>>> a is b
True
>>> a is not b
False
>>> s=[1,2,3,4,5]
>>> r=[1,2,3,4,5]
>>> id(s),id(r)
(1762162202176, 1762162133312)
>>> s==r
True
>>> s!=r
False
>>> s is r
False
>>> s is not r
True
>>> s=[1,2,3,4,5]
>>> r=[2,3,5,6]
>>> id(s),id(r)
(1762118390144, 1762162202176)
>>> s==r
False
>>> s!=r
True
>>> s is r
False
>>> s is not r
True
>>> KeyboardInterrupt
