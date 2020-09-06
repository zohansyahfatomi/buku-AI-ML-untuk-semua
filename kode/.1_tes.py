import random as ran
import math as m

def heart(n):
    rho = 1.0
    cacah = 0.0
    x1 = 0.0
    y1 = 0.0
    z1 = 0.0
    vb = 6*4*5
    i = 1

    for i in range(0,n,1):
        x = ran.uniform(-3, 3)
        y = ran.uniform(-1, 3)
        z = ran.uniform(-2, 3)

        r = (2*x**2 + y**2 + z**2 -1)**3 - 0.1*x**2*z**3 - y**2 *z**3

        if(r <= 0.0):
            x1 = x1 + x*rho
            y1 = y1 + y*rho
            z1 = z1 + z*rho
            cacah = cacah+1

    mt = vb *cacah/n
    vt = mt/rho

    x2 = vb*x1/n
    y2 = vb*y1/n
    z2 = vb*z1/n

    x_cm = x2/mt
    y_cm = y2/mt
    z_cm = z2/mt
    print(x_cm, y_cm, z_cm,vt)

#print("x , y , z, vt")
for i in range(1,31,1):
    heart(100000)
