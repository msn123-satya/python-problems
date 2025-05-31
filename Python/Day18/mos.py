Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='varsha jay'
s.capitalize()
'Varsha jay'
s.upper()
'VARSHA JAY'
s.lower()
'varsha jay'
s.title()
'Varsha Jay'
s.isupper()
False
s.islower()
True
s.isalpha()
False
s.isdigit()
False
s="12345"
s.isdigit()
True
s.isalpha()
False
s="ABCD123"
s.isalpha
<built-in method isalpha of str object at 0x000001C5EEE3D6E0>
s.isalpha()
False
s.isdigit
<built-in method isdigit of str object at 0x000001C5EEE3D6E0>
s.isdigit()
False
s.isalnum
<built-in method isalnum of str object at 0x000001C5EEE3D6E0>
s.isalnum()
True
s="GoOd MoRniNg AlL"
r=s.split()
r
['GoOd', 'MoRniNg', 'AlL']
s="1,2,3,4,5"
r=s.split()
r
['1,2,3,4,5']
s=["MBA","MA","BBA']
   
SyntaxError: unterminated string literal (detected at line 1)
s=["MBA","MA","BBA"]
   
r="-".join(s)
   
r
   
'MBA-MA-BBA'
s=["MBA","MA","BBA"]
   
r=" ".join(s)
   
r
   
'MBA MA BBA'
s="srikakulam vizianagaram"
   
s.count("a")
   
6
s.count("a",10,15)
   
0
s.index('v")
        
SyntaxError: unterminated string literal (detected at line 1)
s.index("v")
        
11
s.index('j')
        
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    s.index('j')
ValueError: substring not found
s.find("j")
        
-1
s.find("z")
        
13
s.rfind("a")
        
21
s.rfind('a',10,19)
        
17
s.startswith('s')
        
True
s.endswith('m')
        
True
s="AP cm is jagan"
        
s.replace("jagan","cbn")
        
'AP cm is cbn'
s.replace('cm','ck')
        
'AP ck is jagan'
s="liril"
        
s.replace("i","k")
        
'lkrkl'
s="guntur amaravathi"
        
s.rstrip()
        
'guntur amaravathi'
s.lstrip()
        
'guntur amaravathi'
s=" guntur amaravathi"
        
s.rstrip()
        
' guntur amaravathi'
s.lstrip()
        
'guntur amaravathi'
s="VARsha"
        
s.swapcase()
        
'varSHA'
s="JAYARAM"
        
s.center(11,"#")
        
'##JAYARAM##'
s.center(20,"%")
        
'%%%%%%JAYARAM%%%%%%%'
s="lokesh"
        
s.rjust(20)
        
'              lokesh'
s.ljust(20)
        
'lokesh              '
s="Lokesh It")
   
SyntaxError: unmatched ')'
s="Lokesh It"
   
s.istitle()
   
True
s=''
   
s.isspace()
   
False
s=" "
   
>>> s.isspace()
...    
True
>>> s=
...    
SyntaxError: invalid syntax
>>> s="India won finals with south africa"
...    
>>> s.split(" ",4)
...    
['India', 'won', 'finals', 'with', 'south africa']
>>> s.split(" ",3)
...    
['India', 'won', 'finals', 'with south africa']
>>> s.rsplit()
...    
['India', 'won', 'finals', 'with', 'south', 'africa']
>>> s.rsplit(" ",4)
...    
['India won', 'finals', 'with', 'south', 'africa']
>>> s.rsplit(" ",3)
...    
['India won finals', 'with', 'south', 'africa']
>>> s="lokesh"
...    
>>> print("%s",%s)
...    
SyntaxError: invalid syntax
>>> print("%s"%s)
...    
lokesh
>>> print("%2s"%s)
...    
lokesh
>>> print("15%s"%s)
...    
15lokesh
>>> print("%15s",%s)
...    
SyntaxError: invalid syntax
>>> print("%15s"%s)
...    
         lokesh
>>> print("%30s"%s)
...    
                        lokesh
