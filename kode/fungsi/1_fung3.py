i = 3 #variabel global
def jangkauan():
    j = 4 #variabel lokal
    print(f'variabel lokal : {j}')
    print(f'variabel global : {i}')
    print(f'variabel built-in : {dir}')

jangkauan()
print(i)
print(dir)
print(j)#terjadi kesalahan