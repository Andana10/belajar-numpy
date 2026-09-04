import numpy as np

def materi():
      #Transpose (Recap dari M3) + Determinant & Inverse
      A = np.array([[4, 2], [7, 6]])

      print(np.linalg.det(A))   # determinant: 4*6 - 2*7 = 10
      print(np.linalg.inv(A))   # invers matriks (kayak "1/A" versi matriks)

      #Kegunaan inverse: Menyelesaikan sistem persamaan linear, dan jadi dasar dari Normal Equation untuk linear regression (lihat studi kasus di bawah).

      #Menyelesaikan Sistem Persamaan Linear
      # Sistem: 2x + y = 5 ; x + 3y = 10
      A = np.array([[2, 1], [1, 3]])
      b = np.array([5, 10])
      x = np.linalg.solve(A, b)
      print(x)  # [1. 3.] -> x=1, y=3

      #Eigenvalues & Eigenvectors
      #Konsep ini dasar dari PCA (Principal Component Analysis) — teknik reduksi dimensi yang sangat umum di ML:

      A = np.array([[2, 0], [0, 3]])
      eigenvalues, eigenvectors = np.linalg.eig(A)
      print("Eigenvalues:", eigenvalues)
      print("Eigenvectors:\n", eigenvectors)

#soal 11
#hitung determinan
A = np.array([[3, 1], [2, 4]])
det = np.linalg.det(A)
print(det)  # 10.0

#soal 12
A = np.array([[3, 2], [1, -1]])
b = np.array([12, 1])
solusi = np.linalg.solve(A, b)
print(solusi)

#soal 13
A = np.array([[4, 2], [1, 3]])
invers = np.linalg.inv(A)
print(invers)
identitas = A @ invers
print(np.round(identitas, decimals = 10))