import numpy as np

def jacobi(M,l):
    batas_iter = 1000

    print("Sistem:")
    for i in range(M.shape[0]):
        row = ["{}*x{}".format(M[i, j], j + 1) for j in range(M.shape[1])]
        print(" + ".join(row), "=", l[i])
    print()

    k = np.zeros_like(l)
    for it_count in range(batas_iter):
        print("Solusi ke ",it_count," :", k)
        k_new = np.zeros_like(k)

        for i in range(M.shape[0]):
            s1 = np.dot(M[i, :i], k[:i])
            s2 = np.dot(M[i, i + 1:], k[i + 1:])
            k_new[i] = (l[i] - s1 - s2) / M[i, i]

        if np.allclose(k, k_new, atol=1e-8, rtol=0.):
            break

        k = k_new

    print("Solusi:")
    print(k)
    error = np.dot(M, k) - l
    print("Kesalahan:")
    print(error)

# mendeskripsikan matriks
M = np.array([[10., 1., 1., 1., 1.],
              [1., 10., 1., 1., 1.],
              [1., 1., 10., 1., 1.],
              [1., 1., 1., 10., 1.],
              [1., 1., 1., 1., 10.],
              ])

K = np.array([14., 14., 14., 14.,14])

jacobi(M,K)