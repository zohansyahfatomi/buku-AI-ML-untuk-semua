import numpy as np
import matplotlib.pyplot as plt


def fungsi(x):
    fungsi = np.cos(x)
    return fungsi

def dfungsi(x):
    dfungsi = -np.sin(x)
    return dfungsi

def dfung(x,h):
    dfung_maju=(fungsi(x+h)-fungsi(x))/h
    dfung_mundur=(fungsi(x)-fungsi(x-h))/h
    dfung_terpusat=(fungsi(x+h)-fungsi(x-h))/(2*h)
    return dfung_maju,dfung_mundur,dfung_terpusat

def plot_fungsi(a,b,n):
    x_i=np.linspace(a,b,n)
    f=np.zeros(n)
    for i in range(0,n,1):
        x=x_i[i]
        f[i]=fungsi(x)
        print(x,f[i])
    plt.plot(x_i,f,'k',label="Kurva fungsi")
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.title('Kurva f(x) = cos(x)')
    plt.legend()
    plt.show()

def plot_dfung(a,b,n):
    (x_i,h)=np.linspace(a,b,n,retstep=True)
    dff=np.zeros(n)
    dfb=np.zeros(n)
    dfc=np.zeros(n)
    dfeksak=np.zeros(n)

    for i in range(0,n,1):
        x=x_i[i]
        (dfung_maju,dfung_mundur,dfung_terpusat)=dfung(x,h)
        dff[i]=dfung_maju
        dfb[i]=dfung_mundur
        dfc[i]=dfung_terpusat
        dfeksak[i]=dfungsi(x)
        print(x, dff[i], dfb[i],dfc[i],dfeksak[i])

    plt.plot(x_i,dff,'y--',label="Maju")
    plt.plot(x_i,dfb,'r--',label="Mundur")
    plt.plot(x_i,dfc,'b--',label="Terpusat")
    plt.plot(x_i,dfeksak,'k',label="Hasil Eksak")
    plt.title('Kurva f\'(x) = -sin(x)')
    plt.xlabel('x')
    plt.ylabel('Turunan Pertama')
    plt.legend()
    plt.show()

plot_fungsi(0,10,100)
plot_dfung(0,10,100)
