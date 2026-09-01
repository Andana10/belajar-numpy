import numpy as np

def materi():
      data = np.array([23, 45, 12, 67, 34, 89, 21])

      print(np.median(data))       # nilai tengah -> lebih tahan outlier daripada mean
      print(np.percentile(data, 25))  # kuartil 1 (Q1)
      print(np.percentile(data, 75))  # kuartil 3 (Q3)
      print(np.var(data))          # variance (std kuadrat)


      #KORELASI DAN KOVARIANS
      jam_belajar = np.array([1, 2, 3, 4, 5])
      nilai_ujian = np.array([50, 55, 65, 70, 85])

      korelasi_matrix = np.corrcoef(jam_belajar, nilai_ujian)
      print(korelasi_matrix)
      # [[1.        0.98      ]
      #  [0.98      1.        ]]

#soal 5
gaji = np.array([5000000, 5500000, 4800000, 6000000, 500000000])
print("Median:", np.median(gaji)) #jauh lebih representatif
print("Rata2:", np.mean(gaji)) #sangat terpengaruh outlier!

#soal 6
luas_rumah = np.array([50, 70, 90, 120, 150])
harga_rumah = np.array([300, 420, 550, 700, 900])
korelasi = np.corrcoef(luas_rumah, harga_rumah)
print(korelasi[0, 1])  # ambil nilai korelasi (bukan diagonal) -> sekitar 0.998
#artinya luas rumah dan harga rumah punya hubungan linear yang SANGAT kuat 

#soal 7
nilai = np.array([45, 60, 65, 70, 72, 75, 78, 80, 85, 95])
Q1 = np.percentile(nilai, 25)
Q3 = np.percentile(nilai, 75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

mask_outlier = (nilai < batas_bawah) | (nilai > batas_atas)
print("Outlier:", nilai[mask_outlier])