import numpy as np

#soal 18
nilai = np.array([[80,90],
                  [70,85],
                  [95,60]]) #(3, 2) 3 siswa 2 mapel
print(nilai.T) #(2, 3)

#soal 19
arr = np.array([[1,2],[3,4]])
arr_T = arr.T
arr_T[0,0] = 999
print(arr)
# [[999   2]
#  [  3   4]] -> IKUT BERUBAH karena .T adalah view

#soal 20
arr = np.array([[1,2,3,4,5]])  # shape (1,5)
print(arr.shape)  # (1, 5)

arr_squeezed = arr.squeeze() #menghilangkan dimensi yang berisi '1', supaya jadi (5,)
print(arr_squeezed.shape)  # (5,)
