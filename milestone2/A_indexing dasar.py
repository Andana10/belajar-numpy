import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[0]) #elemen pertama
print(arr[-1]) #elemen terakhir

#soal 2
arr[2] = 99
print(arr)

#soal 3
nilai = np.array([65, 70, 55, 80, 90, 45, 100])
print(nilai[:3]) #awal samapi index 3
print(nilai[-3:]) #3 dari belakang sampai akhir

#soal 4
print(nilai[::2])#step 2

#soal 5
#[start: end: step]
balik = nilai[::-1] #membalik nilai dari belakang ke depan
print(balik)
