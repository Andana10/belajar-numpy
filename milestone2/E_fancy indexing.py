import numpy as np 

#soal 19
arr = np.array([100, 200, 300, 400, 500])
print(arr[[0, 2, 4]]) #ambil elemen ke 0, 2, 4 dengan memasukkan [list index] ke []

#soal 20
b = arr[[0, 2, 4]]
b[0] = 99
print(arr) # [100 200 300 400 500] -> TIDAK berubah, karena fancy indexing = copy

#soal 21
suhu = np.array([28, 31, 35, 22, 40, 19])
#membuat boolean mask
mask = suhu > 25
print(mask.sum()) #menghitung jumlah true
