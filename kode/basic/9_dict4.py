greek = {1 : "alpha", 2:"beta", 3:"gamma"}
print(greek.get(1))
print(greek.get(4,"zeta"))
print(greek.items())

greek.pop(1)
print("Hasil dari pop() : ",greek)

greek.update({1:"tetha"})
print("Hasil dari update() : ",greek)

print("Cetak nilai dari dict greek : ",greek.values())

print("Cetak kunci dari dict greek : ",greek.keys())

greek.clear()
print("Hasil dari clear() : ", greek)

