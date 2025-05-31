n=float(input("enter power consumed in units:"))
if((n>=0) and (n<50)):
    print("Pay: 100 rupees")
elif((n>=50) and (n<100)):
    print("pay:",100+(n-50)*2,"rupees")
elif((n>=100) and (n<150)):
    print("pay:",100+50*2+(n-100)*2.5,"rupees")
elif((n>=150) and (n<=200)):
    print("pay:",100+50*2+50*2.5+(n-150)*3,"rupees")
else:
    print("pay:",100+50*2+50*2.5+50*3+(n-200)*4,"rupees")

