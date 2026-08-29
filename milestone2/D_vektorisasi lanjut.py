import numpy as np

#soal 14
harga = np.array([15000, 22000, 8000, 30000, 12000])
stok = np.array([10, 5, 20, 3, 15])
total_nilai = harga * stok
print(total_nilai.sum())

#soal 15
suhu = np.array([15, 22, 28, 33, 19, 25, 30])
suhu_capped = np.where(suhu > 30, 30, suhu) #np.where(kondisi, nilai_jika_true, nilai_jika_false): "Kalau suhu > 30, ganti jadi 30, kalau nggak, biarin nilai aslinya."
print(suhu_capped)

#soal 16
suhu = np.array([15, 22, 28, 33, 19, 25, 30])
suhu_clipped = np.clip(suhu, 18, 30) #dibawah 18 akan menjadi 18, diatas 30 menjadi 30
print(suhu_clipped) 

#soal 17
produk = np.array(["Sabun", "Shampo", "Pasta Gigi", "Sikat Gigi"])
harga = np.array([5000, 25000, 8000, 12000])
index_max = harga.argmax()
print(produk[index_max])
 
#soal 18
nilai = np.array([55, 70, 88, 45, 92, 60, 78])
galulus = np.where(nilai < 60, 0, nilai)
print(galulus)