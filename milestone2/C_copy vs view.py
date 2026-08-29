import numpy as np

#soal 11
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 99
print(a)  # [ 1 99  3  4  5] -> IKUT BERUBAH!
# slicing di NumPy menghasilkan view, bukan copy baru. 
# b itu cuma "jendela" yang nunjuk ke memori yang sama
# dengan a. Ini beda banget sama Python list biasa! 

#soal 12 
a = np.array([1, 2, 3, 4, 5])
b = a[1:4].copy()
print(a)  # [1 2 3 4 5] -> TIDAK berubah
print(b)  # [99  3  4]

#soal 13
a = np.array([1, 2, 3, 4, 5])
view = a[1:4]
copy = a[1:4].copy()

print(view.base is a)  # True -> view "menumpang" di memori a
print(copy.base is None)  # True -> copy punya memori sendiri