import numpy as np

#soal 1
harga = np.array([10000, 20000, 30000])
naik = harga + 5000 #array + scalar
print(naik)

#soal 2
matriks = np.array([[1,2,3],[4,5,6]])
print(matriks * 10)

#soal 3
suhu_celcius = np.array([[20, 25], [30, 35]])
F = suhu_celcius * 9/5 + 32
print(F)