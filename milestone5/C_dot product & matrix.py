import numpy as np

def materi():
      #Dot Product(perkalian titik)
      a = np.array([1, 2, 3])
      b = np.array([4, 5, 6])
      hasil = np.dot(a, b)   # 1*4 + 2*5 + 3*6 = 32
      print(hasil)  # 32

      #Matrix Multiplication
      A = np.array([[1, 2], [3, 4]])
      B = np.array([[5, 6], [7, 8]])
      hasil = A @ B
      print(hasil)
      # [[19 22]
      #  [43 50]]

      A * B   # elementwise: [[1*5, 2*6], [3*7, 4*8]] = [[5,12],[21,32]]
      A @ B   # matrix mult:  aturan baris-kali-kolom -> [[19,22],[43,50]]

#soal 8
fitur = np.array([100, 3, 10])
bobot = np.array([2.5, 50, -1.2])

prediksi_harga = np.dot(fitur, bobot) + 10
print(prediksi_harga)

#soal 9
A = np.array([[2,0],[1,3]])
B = np.array([[1,2],[3,4]])
print(A @ B)
print(B @ A)

#soal 10
X = np.array([
    [100, 3],
    [150, 4],
    [80, 2]
])
w = np.array([2.0, 30])
print(X @ w + 5)