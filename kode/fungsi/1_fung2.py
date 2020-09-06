def fact_rec(n):
    if n == 1:
        return 1 #kriteria berhenti
    else :
        return n * fact_rec(n-1)

print(f'factorial dari 6 adalah {fact_rec(6)}')