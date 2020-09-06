def fung(x):
    return x ** 2

def simp13_(a, b, n):
    h = (b - a) / n

    x = list()
    fx = list()

    i = 0
    while i <= n:
        x.append(a + i * h)
        fx.append(fung(x[i]))
        i = i + 1

    integ = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            integ = integ + fx[i]
            print('{:2d}    {:3.8f}    {:3.8f}    {:3.8f}'
                  .format(i, x[i], fung(x[i]), integ))
        elif i % 2 == 0:
            integ = integ + 2 * fx[i]
            print('{:2d}    {:3.8f}    {:3.8f}    {:3.8f}'
                  .format(i, x[i], fung(x[i]), integ))
        else:
            integ = integ + 4 * fx[i]
            print('{:2d}    {:3.8f}    {:3.8f}    {:3.8f}'
                  .format(i, x[i], fung(x[i]), integ))
        i = i + 1
    integ = integ * (h / 3)
    return integ

a = 0
b = 1
n = 10
print(" i        x[i]        f(x[i])        I[i]   ")
hasil = simp13_(a, b, n)
print("Hasil metode Simpson-1/3",hasil)
