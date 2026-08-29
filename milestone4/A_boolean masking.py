import numpy as np

# mask = (suhu > 20) & (suhu < 35)   # BENAR
# mask = suhu > 20 & suhu < 35        # SALAH -> error atau hasil aneh!


#soal 1
nilai = np.array([65, 45, 80, 90, 55, 70, 30])
mask_lulus = nilai >= 60
print(nilai[mask_lulus])

#soal 2
nilai = np.array([65, 45, 80, 90, 55, 70, 30])
tidak_lulus = nilai < 60
print(nilai[tidak_lulus].sum())

#soal 3
umur = np.array([17, 25, 16, 30, 22, 15, 40])
mask = (umur >= 18) & (umur <= 30)
print(umur[mask])

#soal 4
diluar = (umur < 18) | (umur > 30)
print(umur[diluar])

#soal 5
nilai = np.array([65, 45, 80, 90, 55, 70, 30])
tidaklulus = ~mask_lulus
print(nilai[tidaklulus])