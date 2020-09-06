import numpy as np

def gauss_seidel(M,l):
    batas_iter = 1000
    print("Sistem Persamaan :")
    for i in range(M.shape[0]):
        row = ["{0:3g}*x{1}".format(M[i, j], j + 1) for j in range(M.shape[1])]
        print("[{0}] = [{1:3g}]".format(" + ".join(row), l[i]))

    x = np.zeros_like(l)
    for it_count in range(1, batas_iter):
        x_new = np.zeros_like(x)
        print("Iterasi ke-{0}: {1}".format(it_count, x))
        for i in range(M.shape[0]):
            s1 = np.dot(M[i, :i], x_new[:i])
            s2 = np.dot(M[i, i + 1:], x[i + 1:])
            x_new[i] = (l[i] - s1 - s2) / M[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        x = x_new

    print("Solusi: {0}".format(x))
    error = np.dot(M, x) - l
    print("Koreksi: {0}".format(error))

# Mendefinisikan sistem matriks
M = np.array([[10., 1., 1., 1., 1.],
              [1., 10., 1., 1., 1.],
              [1., 1., 10., 1., 1.],
              [1., 1., 1., 10., 1.],
              [1., 1., 1., 1., 10.],
              ])

L = np.array([14., 14., 14., 14., 14.])

gauss_seidel(M,L)