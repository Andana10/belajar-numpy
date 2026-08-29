import numpy as np

# #soal 21
# harga_idr = np.array([50000, 120000, 35000, 200000]) #(4,)
# kurs = np.array([0.000065, 0.000060, 0.0097])  # shape (3,)

# #reshape harga jadi (4, 1) biar bisa broadcast dengan (3,) menjadi (4, 3)
# matriks = harga_idr.reshape(4, 1) * kurs
# print(matriks)

# #soal 22
# nilai = np.array([
#     [80, 70, 90, 60],
#     [70, 65, 80, 55],
#     [95, 90, 85, 92],
#     [60, 55, 70, 50],
#     [88, 92, 78, 84]
# ])
# rata_per_mapel = nilai.mean(0) #rata-rata per kolom (shape(4,))
# std_per_mapel = nilai.std(0) 
# z_score = (nilai - rata_per_mapel) / std_per_mapel
# print(z_score)

#soal 23
bulan1 = np.array([
    [100, 120, 90, 110],   # Toko A, minggu 1-4
    [80, 85, 95, 100],     # Toko B
    [150, 160, 140, 155]   # Toko C
])
bulan2 = np.array([
    [105, 115, 95, 120],
    [90, 88, 92, 98],
    [155, 165, 145, 160]
])
gabung = np.stack([bulan1, bulan2]).reshape(2, 3, 4)
print(gabung)
total_per_toko = gabung.sum(axis=(0, 2))
print(total_per_toko)