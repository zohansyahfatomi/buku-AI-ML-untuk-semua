def fung(x):
    return x**2

def simp38(a,b,n):
    h = (float(b - a) /n)
    integ = fung(a) + fung(b);
    for i in range(0,n):
        if (i % 3 == 0):
            integ = integ + 2 * fung(a + i * h)
            print('{:2d}    {:3.8f}    {:3.8f}    {:3.8f}'
                  .format(i, a+i*h, fung(a+i*h), ((float(3 * h) / 8) * integ)))
        else:
            integ = integ + 3 * fung(a + i * h)
            print('{:2d}    {:3.8f}    {:3.8f}    {:3.8f}'
                  .format(i, a + i * h, fung(a + i * h), ((float(3 * h) / 8) * integ)))
    return ((float(3 * h) / 8) * integ)

n = 10
a = 0
b = 1

print(" i        x[i]        f(x[i])        I[i]   ")
hasil = simp38(a,b,n)
print("Hasil metode Simpson-3/8",hasil)


