import numpy as np
import matplotlib.pyplot as plt

def integmc (f, a, b, n):
    x = np.arange(a,b, 0.001)
    y = f(x)
    f_max = max(y)

    x_rand = a + np.random.random(n)*(b-a)
    y_rand = a + np.random.random(n)*f_max

    t_baw = np.where(y_rand < f(x_rand))
    t_ata = np.where(y_rand >= f(x_rand))

    print("Titik di bawah kurva                :", len(t_baw[0]))
    print("Titik di atas kurva                 :", len(t_ata[0]))
    print("Titik di bawah kurva/Total titik    :", len(t_baw[0])/n)
    print("Luas selimut kurva (Persegi panjang):", f_max*(b-a))
    print("Integral                            :", f_max*(b-a)*len(t_baw[0])/n)

    #plot
    plt.plot(x, y, color="black", linewidth=2, label = "$f(x) = x^2$")
    plt.scatter(x_rand[t_baw], y_rand[t_baw], color="black", s=1, label="Titik di bawah kurva")
    plt.scatter(x_rand[t_ata], y_rand[t_ata], color="gray", s=1, label="Titik di atas kurva")
    plt.legend(loc="best")
    plt.show()

def f(x):
    return x**2

a = 0
b = 1
n = 10000
integmc(f,0,1,10000)
