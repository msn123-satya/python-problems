import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
s=0.33
g=9.81
gc=1
mue=10**-3
x=6
Do=float(input("outer diameter in mm:"))
Do=Do*(10**-3)
Di=float(input("inner diameter in mm:"))
Di=Di*(10**-3)
L=float(input("packed bed height in cm:"))
L=L*(10**-2)
h=float(input("length of rashig in cm:"))
h=h*(10**-2)
D=float(input("Diameter of column in mm:"))
D=D*(10**-3)
t=float(input("time in s:"))
#vw=float(input("volume of water:"))
#vp=float(input("volume of packings:"))
#TV=float(input("Total Volume:"))
Pa=13600#density of mercury
Pb=1000#density of water
l1,l2,l3,l4,l5,l6=[],[],[],[],[],[]
n=6
i=0
Rm=list(map(float,input("enter manometer readings in cm   :").split()))[:6]
Q=list(map(float,input("volumetric flow rate in LPM       :").split()))[:6]
while(n>0) and (i<6):
    Rm1=Rm[i](10*-2)
    q=(Q[i]10*-3)/60   
    l1.append(q)
    A=(math.pi*D**2)/4
    Vo=q/A
    l3.append(Vo)
    Sp=math.pi*(Do+Di)*(h+t)
    Vp=math.pi*((Do*2)-(Di2))(h/4)
    Dp=(6*Vp)/(s*Sp)
    dP=Rm1*(Pa-Pb)*g
    l2.append(dP)
    Rep=(Dp*Vo*Pb)/mue
    obRep=(1/Rep)(10*-3)
    l4.append(Rep)
    l6.append(obRep)
    E=0.694
    Fp=(s*dP*Dp*(E*3)*gc)/(Pb*L(Vo*2)(1-E))
    l5.append(Fp) 
    x=x-1
    i=i+1
df = pd.DataFrame({'flow rate':l1,'pressure drop':l2,'Superficial Velocity(Vo)':l3,'Particle Reynold Number (Rep)':l4,'Friction factor(Fp)':l5,'one by Rep':l6})
print(df)
xpoints = np.array(l6)
ypoints = np.array(l5)
plt.plot(xpoints, ypoints)
plt.show()
