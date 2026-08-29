import numpy as np

# Broadcasting
# The dimensions have the same size
# OR
# One of the dimensions has a size of 1

#soal 4
nilai = np.array([
    [80, 70],
    [90, 85],
    [75, 95] #shape(3,2)
])

bobot = np.array([0.4, 0.6])  # shape (2,)
nilai_terbobot = nilai * bobot
print(nilai_terbobot)

nilai_akhir = nilai_terbobot.sum(1) #menjumlahkan perbaris
print(nilai_akhir)
#NumPy "menyamakan" bobot jadi seolah (3,2) dengan cara mengulang barisnya 3 kali
    # [80, 70]    [0.4, 0.6]  
    # [90, 85] +  [0.4, 0.6]
    # [75, 95]    [0.4, 0.6]


#soal 5
matriks = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]]) #(3,3)
kolom_vector = np.array([[10],
                         [20],
                         [30]]) #(3,1)
tambah = matriks + kolom_vector
print(tambah)

#soal 6
try:
    hasil = np.array([1,2,3]) + np.array([1,2])
except ValueError as e:
    print("Error:", e)
# ValueError: operands could not be broadcast together with shapes (3,) (2,)
 
#soal 7
suhu = np.array([
    [30, 32, 31, 29],  # Jakarta
    [22, 21, 23, 20],  # Bandung
    [28, 29, 27, 30]   # Surabaya
])
rata_per_kota = suhu.mean(1)
print(rata_per_kota.shape) #shape(3,) 3 elemen dalam 1 baris
rata_per_kota_2d = rata_per_kota.reshape(3, 1) #ubah menjadi 3 baris 1 kolom

deviasi = suhu - rata_per_kota_2d
print(deviasi)