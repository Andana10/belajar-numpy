import numpy as np

#A. Membuat array dari python list

#array 1D (vektor)
arr_1d = np.array([10, 20, 30, 40])
print("Array 1D:", arr_1d)
"""
ndim: Jumlah dimensi (1D = vektor, 2D = matriks, 3D = tensor/kubus).
shape: Ukuran tiap dimensi (misal: (3, 4) artinya 3 baris dan 4 kolom).
size: Total jumlah elemen di dalam array.
dtype: Tipe data elemen (misal: int64, float64).
"""
print(f"Shape: {arr_1d.shape} | Dimensi: {arr_1d.ndim}\n")

#Array 2D (matriks: 2 baris, 3 kolom)
arr_2d = np.array([
      [1, 2, 3],
      [4, 5, 6]
])
print("Array 2D:\n", arr_2d)
print(arr_2d.ndim, arr_2d.shape)

arr_3d = np.array([
      [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
       ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R'],
       ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '']]
])

print(arr_3d.ndim, arr_3d.shape)

# -------------------------------------------------------------
# B. Membuat Array dengan Built-in Functions (Sangat Sering Dipakai)
# -------------------------------------------------------------
# 1. Array berisi Nol (2 baris, 4 kolom) - cocok untuk inisialisasi awal
zeros = np.zeros((2, 4))

# 2. Array berisi Angka Satu (3 baris, 2 kolom)
ones = np.ones((3, 2))

# 3. Rentang Angka dengan Step: np.arange(start, stop, step)
# Membuat angka dari 0 sampai 8 dengan loncatan 2
rentang = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# 4. Angka Terbagi Rata: np.linspace(start, stop, num_of_points)
# Membagi rentang 0 sampai 1 menjadi 5 bagian yang jaraknya persis sama
garis = np.linspace(0, 1, 5)   # [0.  , 0.25, 0.5 , 0.75, 1.  ]

print("Zeros (2x4):\n", zeros)
print("Arange (step 2):", rentang)
print("Linspace (0 ke 1, 5 poin):", garis)


#kuis
array2d = np.arange(9).reshape(3, 3)
print(array2d)

suhu = np.array([28, 31, 35, 22, 40, 19])
mask = (suhu < 25) | (suhu >35)
print(mask)           # [False True True False True False]
print(suhu[mask])     # [31 35 40] -> cuma suhu di atas 30