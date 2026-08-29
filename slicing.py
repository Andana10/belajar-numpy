import numpy as np

#Membuat matriks 3x4 (0 samapi 11)
matrix = np.arange(12).reshape(3, 4)
# print(matrix)
# # [[ 0,  1,  2,  3],
# #  [ 4,  5,  6,  7],
# #  [ 8,  9, 10, 11]]

# #array[start:end:step]

# #Ambil elemen baris ke-1, kolom ke-2 -> Nilai: 6
# print(matrix[1, 2])

# #Ambil seluruh baris ke-0 -> [0, 1, 2, 3]
# print(matrix[0, :])

print(matrix[0])

# #Slicing sub matriks: baris 0-1, kolom 1-2
# print(matrix[0:2, 1:3])
