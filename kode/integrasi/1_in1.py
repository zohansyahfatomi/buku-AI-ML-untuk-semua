def fung(x):
    return x**2

def trape(f, a, b, n):
    h = (b-a)/float(n)

    integ = 0.5*(f(a) + f(b))

    for i in range(1,n,1):
        integ = integ + f(a + i*h)
        print('{:2d}    {:3.8f}    {:3.8f}    {:3.8f}    {:3.8f}'
              .format(i, a+i*h, h, f(a+i*h) ,integ))
    return h*integ

a = 0;  b = 1
n = 10
print(" i       x_i             h          f(x_i)         I_s ")
hasil = trape(fung, a, b, n)
print("Hasil metode Trapezoidal",hasil)