def metode_gauss(M):
    n = len(M)

    for i in range(0, n):
        max_elemen = abs(M[i][i])
        maxBaris = i
        for k in range(i+1, n):
            if abs(M[k][i]) > max_elemen:
                max_elemen = abs(M[k][i])
                maxBaris = k

        for k in range(i, n+1):
            tmp = M[maxBaris][k]
            M[maxBaris][k] = M[i][k]
            M[i][k] = tmp

        for k in range(i+1, n):
            c = -M[k][i]/M[i][i]
            for j in range(i, n+1):
                if i == j:
                    M[k][j] = 0
                else:
                    M[k][j] += c * M[i][j]

    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = M[i][n]/M[i][i]
        for k in range(i-1, -1, -1):
            M[k][n] -= M[k][i] * x[i]
    return x

def cetak(M):
    n = len(M)
    for i in range(0, n):
        garis = ""
        for j in range(0, n+1):
            garis += str(M[i][j]) + "\t"
            if j == n-1:
                garis += "| "
        print(garis)
    print("")

if __name__ == "__main__":
    from fractions import Fraction
    n = input()

    M = [[0 for j in range(n+1)] for i in range(n)]
    for i in range(0, n):
        garis = map(Fraction, raw_input().split(" "))
        for j, el in enumerate(garis):
            M[i][j] = el
    raw_input()

    garis = raw_input().split(" ")
    lastLine = map(Fraction, garis)
    for i in range(0, n):
        M[i][n] = lastLine[i]

    cetak(M)

    x = metode_gauss(M)

    garis = "Hasil Perhitungan:\t"

    for i in range(0, n):
        garis += str(x[i]) + "\t"
    print(garis)



