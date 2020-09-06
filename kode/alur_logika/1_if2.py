nilai = float(input("Masukan nilai Anda : "))
if nilai < 0 or nilai > 1:
    print("salah input")
elif nilai > .9 :
    print("Nilai Anda adalah A")
elif nilai > .8 :
    print("Nilai Anda adalah B")
elif nilai > .7 :
    print("Nilai Anda adalah C")
elif nilai > .6 :
    print("Nilai Anda adalah D")
else :
    print("Nilai Anda adalah E")