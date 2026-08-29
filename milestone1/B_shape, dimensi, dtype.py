import numpy as np

#soal 6
#berapa .ndim, .shape, .size
data = np.array([[1, 2, 3], 
                 [4, 5, 6]])
print(data.ndim) #1D
print(data.shape) #(2, 3) 2 baris 3 kolom
print(data.size) #6

#soal 7
nilai = np.array([80, 90.5, 70])
print(nilai.dtype) #upgrade ke float karena tipe harus sama semua

#soal 8
float = np.array([1, 2, 3], dtype = np.float32) #paksa array supaya dtypenya float32
print(float.dtype)
print(float)

#soal 9
arr3d = np.random.rand(2, 3, 4)
print(arr3d)
print(arr3d.ndim)   # 3
print(arr3d.shape)  # (2, 3, 4) 2 lembar tabel 3x4

#soal 10, Berapa ukuran memori total array ini dalam byte?
arr = np.array([1, 2, 3])
print(arr.itemsize) #8 (byte per elemen, karena int64)
print(arr.nbytes) #24 (3 elemen x 8 byte)