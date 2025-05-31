'''import math
class Test:
    a=100
    def __init__(self,b):
        self.b=b
    def ap(self,l):
        self.l=l
        self.l.append(5)
        print(self.l)
        self.l.sort()
        print(self.l)
        print(Test.a,self.b)
    def ap1(d,r):
        s=d.intersection(r)
        print(s)
        print(Test.a)
    @classmethod
    def ap2(cls):
        print(math.factorial(int(input("enter n:"))))
        print(Test.a)
t1=Test(20)
t1.ap([1,2,4,8,9])
Test.ap1({1,2,3,4,5},{3,4,5,6,7})
Test.ap2()

#To find out the day based on the date
import calendar
days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
l=list(map(int,input().split()))
month,date,year=l
s=calendar.weekday(year,month,date)
print(days[s])

import calendar
d=calendar.month(2024,7)
print(d)

import calendar
d=calendar.month(2022,4)
print(d)

import calendar
d=calendar.calendar(2004)
print(d)'''

import datetime
ct=datetime.datetime.now().time()
print(ct)

