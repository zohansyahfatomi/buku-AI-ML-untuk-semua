import numpy as np

def gauss_elimiminasi(m,k):
    n = len(k)

    #eliminasi
    for p in range(0, n-1):
        for q in range(p+1,n):
            if m[q,p] != 0.0:
                kons = m[q,p]/m[p,p]
                m[q,p+1:n] = m[q,p+1:n] - kons*m[p,p+1:n]
                k[q] = k[q] - kons*k[p]

    #subtitusi balip
    for p in range(n-1, -1, -1):
        k[p] = (k[p] - np.dot(m[p,p+1:n],k[p+1:n]))/m[p,p]
    return k

#mendefinisikan matriks
M = np.array([[12,3,0,0,0,0,0],
              [3,10,3,0,0,0,0],
              [0,3,6,2,0,0,0],
              [0,0,2,4,1,0,0],
              [0,0,0,1,6,1,0],
              [0,0,0,0,1,10,2],
              [0,0,0,0,0,2,12],
              ])

L = np.array([0.116, 1.054, 1.8, 6, 1.8, 1.054, 0.116])

#mencetak hasil
print("Matriks Persegi [M]")
print(M)
print("Matriks [l]")
print(L)
print("Solusi [k]")
print(gauss_elimiminasi(M,L))