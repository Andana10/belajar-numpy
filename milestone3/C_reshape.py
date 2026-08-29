import numpy as np

#soal 8
arr1d = np.arange(1, 13)
print(arr1d.reshape(3, 4)) #mengubah bentuk menjadi 3 baris 4 kolom
print(arr1d.reshape(4, 3)) #4 baris 3 kolom

#soal 9
#-1 artinya "hitung otomatis sisanya"
print(arr1d.reshape(3, -1)) # otomatis hitung -1 = 4
print(arr1d.reshape(-1, 6)) # otomatis hitung -1 = 2

#soal 10
arr = np.arange(1, 13)
try:
    arr.reshape(5, 3)
except ValueError as e:
    print("Error:", e)
# ValueError: cannot reshape array of size 12 into shape (5,3)
# Total elemen HARUS sama. 5 x 3 = 15, tapi array cuma punya 12 elemen.

#soal 11
matriks = np.arange(1, 7).reshape(2, 3)

flat = matriks.flatten()
rav = matriks.ravel()

flat[0] = 999
rav[0] = 888

print(matriks)
# [[888   2   3]
#  [  4   5   6]]
print(flat)  # [999   2   3   4   5   6] -> TIDAK terhubung ke matriks (copy)
print(rav)   # [888   2   3   4   5   6] -> terhubung ke matriks (view)

#soal 12
arr = np.array([1, 2, 3]) #shape (3,)
cara1 = arr.reshape(3, 1)
cara2 = arr[:, np.newaxis]
print(cara1) #(3, 1)
print(cara2) #(3, 1)