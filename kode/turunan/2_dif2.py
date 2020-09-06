import numpy as np
import matplotlib.pyplot as plt

g = 1
l = 1
w = np.sqrt(g/l)
T = 2*np.pi/w
dt = T/2000
t = 2*T
jumlah_t = int(round(t/dt))
t = np.linspace(0, jumlah_t*dt, jumlah_t+1)

x = np.zeros(jumlah_t+1)
v = np.zeros(jumlah_t+1)

x[0] = 0
v[0] = 2

for j in range(jumlah_t):
    x[j+1] = x[j] + dt*v[j]
    v[j+1] = v[j] - w**2*dt*x[j]

fig = plt.figure()
plt.plot(t,x,'k')
plt.ylabel('posisi pegas (rad)')
plt.xlabel('waktu (s)')
plt.show()