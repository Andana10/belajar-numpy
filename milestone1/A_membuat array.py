import numpy as np

#soal 1
# array1d = np.array([5, 10, 15, 20, 25])
# print(type(array1d))
# print(array1d.dtype)

#soal 2
# array = np.arange(10) #membuat array 1 sampa1 9
# print(array)

#soal 3
# array = np.linspace(0, 1, num = 5) #membuat array berisi 5 angka yang merata antara 0 dan 1
# print(array)

#soal 4
#buat array 3x3 isinya semua angka 0, lalu array 2x4 isinya semua angka 1 
nol = np.zeros((3, 3))
satu = np.ones((2, 4))
print(nol)
print(satu)

#soal 5
#membuat array identitas
identitas = np.eye(4) #4x4
print(identitas)