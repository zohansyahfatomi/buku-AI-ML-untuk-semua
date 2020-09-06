female_sc = {"M. Curie", "R. Franklin", "L. Meitner", "J.B. Burnell"}
male_sc = {"A. Einstein", "C. Darwin", "O. Hahn", "G. Galilei"}

male_sc.add("E. Hubble") #menambahkan nilai "E. Hubble" pada set male_sc
print(male_sc)

print("Perpotongan nilai antara female_sc dan male_sc : ",female_sc.intersection(male_sc))

print("Perbedaan nilai antara female_sc dan male_sc : ",female_sc.difference(male_sc))

print("Cek! apakah tidak ada nilai antara female_sc dan male_sc yang sama  : ",female_sc.isdisjoint(male_sc))

print("Gabungkan nilai antara female_sc dan male_sc yang sama  : ",female_sc.union(male_sc))




