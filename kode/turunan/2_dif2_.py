import numpy as np
import matplotlib.pyplot as plt

def euler(y, t, dt, derivs):
    y_next = y + derivs(y,t)*dt
    return y_next

N = 1000 #langkah
x0 =  0.0 #posisi awal pegas
v0 = 0.0 #kecepatan awal
tau = 3.0 #total waktu simulasi
dt = tau/float(N-1) #langkah waktu

k = 3.5 #konstanta pegas, N/m
m = 0.2 #massa, kg
gravity = 9.8 #g, m/s^2

time = np.linspace(0,tau, N)

y = np.zeros([N,2])

y[0,0] = x0
y[0,1] = v0

def SHO(state, time):
    g0 = state[1]
    g1 = -k/m*state[0]-gravity
    return([g0,g1])

for j in range(N-1):
    y[j+1] = euler(y[j], time[j],dt,SHO)

xdata = [y[j,0] for j in range(N)]
vdata = [y[j,1] for j in range(N)]

plt.plot(time, xdata,'k',label='posisi')
plt.plot(time, vdata,'k--',label='kecepatan')
plt.xlabel("Waktu")
plt.ylabel("f(x)/f'(x)")
plt.legend()
plt.show()