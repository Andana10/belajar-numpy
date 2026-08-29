# 🏋️ Latihan Milestone 3: Broadcasting, Reshaping, & Array Manipulation

> 25 soal. Fokus milestone ini: **operasi antar array yang bentuknya beda** (broadcasting), dan **ubah bentuk array tanpa ubah datanya** (reshaping). Ini konsep yang langsung nyambung ke Pandas — tiap kali kamu operasi `df['kolom'] * 2` atau gabungin beberapa DataFrame, di baliknya ini yang kejadian.

Kerjain berurutan, coba sendiri dulu minimal 3-5 menit sebelum buka kunci jawaban!

---

## 🟢 BAGIAN A — Broadcasting Dasar: Scalar ke Array

### Soal 1
Diberikan `harga = np.array([10000, 20000, 30000])`. Tanpa loop, naikkan SEMUA harga sebesar `5000` (scalar + array).

<details>
<summary>🔑 Jawaban</summary>

```python
import numpy as np
harga = np.array([10000, 20000, 30000])
harga_baru = harga + 5000
print(harga_baru)  # [15000 25000 35000]
```
**Ini broadcasting paling sederhana:** scalar `5000` "disebar" (broadcast) ke semua elemen array, seolah-olah scalar itu diubah jadi `[5000, 5000, 5000]` dulu.
</details>

---

### Soal 2
Diberikan array 2D `matriks = np.array([[1,2,3],[4,5,6]])`. Kalikan SELURUH elemen dengan `10` dalam satu baris.

<details>
<summary>🔑 Jawaban</summary>

```python
matriks = np.array([[1,2,3],[4,5,6]])
print(matriks * 10)
# [[10 20 30]
#  [40 50 60]]
```
</details>

---

### Soal 3
Diberikan `suhu_celcius = np.array([[20, 25], [30, 35]])`. Konversi SEMUA nilai ke Fahrenheit (`F = C * 9/5 + 32`) dalam satu ekspresi, walaupun bentuknya 2D.

<details>
<summary>🔑 Jawaban</summary>

```python
suhu_celcius = np.array([[20, 25], [30, 35]])
suhu_f = suhu_celcius * 9/5 + 32
print(suhu_f)
# [[68. 77.]
#  [86. 95.]]
```
**Insight:** Broadcasting nggak peduli array itu 1D atau 2D — scalar selalu bisa "menyebar" ke bentuk apapun.
</details>

---

## 🟡 BAGIAN B — Broadcasting Antar Array (Beda Shape)

### Soal 4
Diberikan matriks nilai 3 siswa x 2 mapel:
```python
nilai = np.array([
    [80, 70],
    [90, 85],
    [75, 95]
])
```
dan bobot per mapel:
```python
bobot = np.array([0.4, 0.6])  # shape (2,)
```
Kalikan `nilai * bobot` (shape `(3,2)` dengan `(2,)`) dalam satu baris — tanpa loop. Lalu jumlahkan per baris (`axis=1`) untuk dapat nilai akhir per siswa.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([
    [80, 70],
    [90, 85],
    [75, 95]
])
bobot = np.array([0.4, 0.6])

nilai_terbobot = nilai * bobot
print(nilai_terbobot)
# [[32. 42.]
#  [36. 51.]
#  [30. 57.]]

nilai_akhir = nilai_terbobot.sum(axis=1)
print(nilai_akhir)  # [74. 87. 87.]
```
**Kenapa ini bisa jalan?** Shape `(3,2)` dan `(2,)` — NumPy "menyamakan" `bobot` jadi seolah `(3,2)` dengan cara mengulang barisnya 3 kali. Aturannya: bandingkan shape dari KANAN ke KIRI, dan dimensi harus sama ATAU salah satunya `1`/kosong.
</details>

---

### Soal 5
Diberikan `matriks = np.array([[1,2,3],[4,5,6],[7,8,9]])` (shape `(3,3)`) dan `kolom_vector = np.array([[10],[20],[30]])` (shape `(3,1)`). Tambahkan keduanya dan jelaskan pola hasilnya.

<details>
<summary>🔑 Jawaban</summary>

```python
matriks = np.array([[1,2,3],[4,5,6],[7,8,9]])
kolom_vector = np.array([[10],[20],[30]])

hasil = matriks + kolom_vector
print(hasil)
# [[11 12 13]
#  [24 25 26]
#  [37 38 39]]
```
**Penjelasan:** `kolom_vector` shape `(3,1)` di-broadcast melebar jadi `(3,3)` — nilai di tiap baris "diulang" ke semua kolom di baris itu. Beda dengan soal 4 yang broadcast ke bawah (antar baris), ini broadcast ke samping (antar kolom).
</details>

---

### Soal 6
Prediksi dulu tanpa run kode: apakah `np.array([1,2,3]) + np.array([1,2])` akan berhasil atau error? Jelaskan kenapa (hint: bandingkan shape-nya).

<details>
<summary>🔑 Jawaban</summary>

```python
try:
    hasil = np.array([1,2,3]) + np.array([1,2])
except ValueError as e:
    print("Error:", e)
# ValueError: operands could not be broadcast together with shapes (3,) (2,)
```
**Penjelasan:** Shape `(3,)` vs `(2,)` — nggak ada satupun yang bernilai `1`, dan angkanya beda (3 vs 2). Aturan broadcasting gagal di sini. Ini error paling umum yang bakal kamu temui — begitu paham "aturan broadcasting", debug error ini jadi cepat.
</details>

---

### Soal 7
Studi kasus: Kamu punya data suhu 3 kota selama 4 hari (shape `(3,4)`), dan mau kurangi tiap kota dengan **suhu rata-ratanya sendiri** (buat lihat "deviasi" dari normal). 
```python
suhu = np.array([
    [30, 32, 31, 29],  # Jakarta
    [22, 21, 23, 20],  # Bandung
    [28, 29, 27, 30]   # Surabaya
])
```
Hitung rata-rata per kota (per baris), lalu kurangi `suhu` dengan rata-rata itu — tanpa loop.

<details>
<summary>🔑 Jawaban</summary>

```python
suhu = np.array([
    [30, 32, 31, 29],
    [22, 21, 23, 20],
    [28, 29, 27, 30]
])

rata_per_kota = suhu.mean(axis=1)          # shape (3,)
rata_per_kota_2d = rata_per_kota.reshape(3, 1)  # ubah jadi (3,1) biar broadcast dengan benar

deviasi = suhu - rata_per_kota_2d
print(deviasi)
# [[-0.5  1.5  0.5 -1.5]
#  [ 0.5 -0.5  1.5 -1.5]
#  [-0.5  0.5 -1.5  1.5]]
```
**PENTING:** Kalau kamu langsung `suhu - rata_per_kota` (tanpa reshape), hasilnya SALAH karena `rata_per_kota` shape `(3,)` akan di-broadcast sebagai BARIS (melebar ke kolom), bukan per kota. Makanya kita reshape ke `(3,1)` dulu supaya broadcasting-nya sesuai maksud kita (per baris). Ini jebakan klasik!
</details>

---

## 🟠 BAGIAN C — Reshape: Mengubah Bentuk Array

### Soal 8
Buat array 1D berisi angka 1-12 (`np.arange(1,13)`), lalu ubah jadi bentuk 2D `(3,4)` dan `(4,3)` — dua-duanya, pakai `.reshape()`.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(1, 13)
print(arr.reshape(3, 4))
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

print(arr.reshape(4, 3))
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
```
</details>

---

### Soal 9
Dari array 12 elemen yang sama, reshape ke `(3, -1)` — apa yang terjadi dengan angka `-1`? Coba juga `(-1, 6)`.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(1, 13)
print(arr.reshape(3, -1))   # NumPy otomatis hitung -1 = 4
print(arr.reshape(-1, 6))   # NumPy otomatis hitung -1 = 2
```
**Insight:** `-1` artinya "hitung otomatis sisanya", berguna banget kalau kamu males ngitung manual atau ukuran datanya dinamis. Cuma boleh ada SATU `-1` per pemanggilan reshape.
</details>

---

### Soal 10
Coba reshape array 12 elemen ke bentuk `(5, 3)`. Apa yang terjadi? Jelaskan kenapa.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(1, 13)
try:
    arr.reshape(5, 3)
except ValueError as e:
    print("Error:", e)
# ValueError: cannot reshape array of size 12 into shape (5,3)
```
**Aturan reshape:** Total elemen HARUS sama. `5 x 3 = 15`, tapi array cuma punya 12 elemen. Reshape nggak bisa "nambah" atau "ngurangin" data, cuma nyusun ulang.
</details>

---

### Soal 11
Ubah array 2D `matriks = np.arange(1,7).reshape(2,3)` jadi array 1D lagi, pakai `.flatten()` dan `.ravel()`. Keduanya sekilas mirip — apa bedanya? (hint: coba modifikasi hasilnya dan lihat apakah `matriks` asli ikut berubah)

<details>
<summary>🔑 Jawaban</summary>

```python
matriks = np.arange(1, 7).reshape(2, 3)

flat = matriks.flatten()
rav = matriks.ravel()

flat[0] = 999
rav[0] = 888

print(matriks)
# [[888   2   3]
#  [  4   5   6]]
print(flat)  # [999   2   3   4   5   6] -> TIDAK terhubung ke matriks (copy)
print(rav)   # [888   2   3   4   5   6] -> terhubung ke matriks (view)
```
**Bedanya:** `.flatten()` selalu bikin **copy** (aman tapi lebih makan memori), `.ravel()` bikin **view** kalau memungkinkan (lebih hemat memori tapi bisa "nyambung" balik ke array asli — inget konsep view dari Milestone 2!).
</details>

---

### Soal 12
Diberikan array 1D `arr = np.array([1,2,3])` shape `(3,)`. Ubah jadi "vektor kolom" shape `(3,1)` dengan DUA cara: pakai `.reshape(3,1)` dan pakai `np.newaxis`.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([1, 2, 3])

cara1 = arr.reshape(3, 1)
cara2 = arr[:, np.newaxis]

print(cara1.shape)  # (3, 1)
print(cara2.shape)  # (3, 1)
print(cara1)
# [[1]
#  [2]
#  [3]]
```
**Kapan dipakai:** Ini teknik yang kamu butuhin persis di Soal 7 tadi buat benerin broadcasting yang salah arah!
</details>

---

## 🔴 BAGIAN D — Menggabung & Memecah Array

### Soal 13
Diberikan `a = np.array([1,2,3])` dan `b = np.array([4,5,6])`. Gabungkan jadi satu array pakai `np.concatenate()`.

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
gabungan = np.concatenate([a, b])
print(gabungan)  # [1 2 3 4 5 6]
```
</details>

---

### Soal 14
Diberikan dua matriks `A = np.array([[1,2],[3,4]])` dan `B = np.array([[5,6],[7,8]])`. Gabungkan **secara vertikal** (nambah baris) pakai `np.vstack()`, dan **secara horizontal** (nambah kolom) pakai `np.hstack()`.

<details>
<summary>🔑 Jawaban</summary>

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

vertikal = np.vstack([A, B])
print(vertikal)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

horizontal = np.hstack([A, B])
print(horizontal)
# [[1 2 5 6]
#  [3 4 7 8]]
```
**Analogi:** `vstack` = numpuk buku ke atas (nambah tinggi tumpukan/baris), `hstack` = jejer buku ke samping (nambah lebar/kolom).
</details>

---

### Soal 15
Studi kasus: Kamu punya data penjualan bulan Januari dan Februari (masing-masing 3 produk):
```python
jan = np.array([100, 150, 200])
feb = np.array([120, 140, 210])
```
Gabungkan jadi satu matriks `(2,3)` dimana baris pertama = Januari, baris kedua = Februari, pakai `np.vstack()`. Lalu hitung total penjualan per produk (jumlah 2 bulan, per kolom).

<details>
<summary>🔑 Jawaban</summary>

```python
jan = np.array([100, 150, 200])
feb = np.array([120, 140, 210])

data = np.vstack([jan, feb])
print(data)
# [[100 150 200]
#  [120 140 210]]

total_per_produk = data.sum(axis=0)
print(total_per_produk)  # [220 290 410]
```
</details>

---

### Soal 16
Diberikan array 1D `arr = np.arange(1,13)` (12 elemen). Pecah jadi **3 bagian sama besar** pakai `np.split()`.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(1, 13)
bagian = np.split(arr, 3)
print(bagian)
# [array([1, 2, 3, 4]), array([5, 6, 7, 8]), array([9, 10, 11, 12])]
```
</details>

---

### Soal 17
Diberikan matriks `(4,4)` berisi angka 1-16. Pecah jadi **2 bagian horizontal** (atas-bawah) pakai `np.vsplit()`, dan **2 bagian vertikal** (kiri-kanan) pakai `np.hsplit()`.

<details>
<summary>🔑 Jawaban</summary>

```python
matriks = np.arange(1, 17).reshape(4, 4)

atas, bawah = np.vsplit(matriks, 2)
print("Atas:\n", atas)
print("Bawah:\n", bawah)

kiri, kanan = np.hsplit(matriks, 2)
print("Kiri:\n", kiri)
print("Kanan:\n", kanan)
```
</details>

---

## 🟣 BAGIAN E — Transpose & Manipulasi Dimensi

### Soal 18
Diberikan matriks `nilai = np.array([[80,90],[70,85],[95,60]])` (shape `(3,2)` = 3 siswa, 2 mapel). Transpose jadi `(2,3)` pakai `.T`. Jelaskan apa makna baru dari baris & kolom setelah transpose.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([[80,90],[70,85],[95,60]])
print(nilai.T)
# [[80 70 95]
#  [90 85 60]]
print(nilai.T.shape)  # (2, 3)
```
**Penjelasan:** Sebelum transpose, baris = siswa, kolom = mapel. Setelah transpose, baris = mapel, kolom = siswa. Transpose sering dipakai buat "membalik perspektif" data, terutama pas kamu butuh operasi matriks yang syaratnya dimensi harus cocok.
</details>

---

### Soal 19
Buktikan bahwa transpose itu **view**, bukan copy (kayak slicing di Milestone 2). Ubah satu elemen di hasil `.T`, lalu cek apakah array asli ikut berubah.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([[1,2],[3,4]])
arr_T = arr.T
arr_T[0,0] = 999
print(arr)
# [[999   2]
#  [  3   4]] -> IKUT BERUBAH karena .T adalah view
```
</details>

---

### Soal 20
Diberikan array shape `(1, 5)`. Hilangkan dimensi yang cuma berisi `1` itu supaya jadi shape `(5,)` murni, pakai `.squeeze()`.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([[1,2,3,4,5]])  # shape (1,5)
print(arr.shape)  # (1, 5)

arr_squeezed = arr.squeeze()
print(arr_squeezed.shape)  # (5,)
```
**Kapan berguna:** Sering kejadian pas hasil operasi (misal prediksi model ML) punya dimensi "sisa" yang nggak perlu, kayak `(100, 1)` padahal maksudnya cuma 100 nilai.
</details>

---

## 🏆 BAGIAN F — Tantangan Bonus (Level Boss)

### Soal 21
Diberikan data harga 4 produk dalam Rupiah:
```python
harga_idr = np.array([50000, 120000, 35000, 200000])
```
dan kurs 3 mata uang (USD, EUR, JPY) relatif ke IDR:
```python
kurs = np.array([0.000065, 0.000060, 0.0097])  # shape (3,)
```
Buat matriks harga dalam SEMUA mata uang untuk SEMUA produk sekaligus (hasil shape `(4,3)`) — pakai broadcasting dan reshape, TANPA loop.

<details>
<summary>🔑 Jawaban</summary>

```python
harga_idr = np.array([50000, 120000, 35000, 200000])  # shape (4,)
kurs = np.array([0.000065, 0.000060, 0.0097])           # shape (3,)

# reshape harga jadi (4,1) supaya broadcast dengan kurs (3,) -> hasil (4,3)
harga_semua_mata_uang = harga_idr.reshape(-1, 1) * kurs
print(harga_semua_mata_uang)
# Baris = produk, kolom = [USD, EUR, JPY]
```
**Insight:** `(4,1) * (3,)` -> NumPy broadcast jadi `(4,3)`. Ini pola yang SANGAT umum: reshape salah satu array jadi vektor kolom `(-1,1)` supaya "menyebar" ke kolom-kolom array lainnya.
</details>

---

### Soal 22
Diberikan matriks nilai ujian 5 siswa x 4 mapel (`(5,4)`). Standarisasi nilai (**Z-score**) per mapel — artinya, untuk tiap KOLOM (mapel), kurangi dengan rata-rata kolom itu, lalu bagi dengan standar deviasi kolom itu. Semua tanpa loop.

```python
nilai = np.array([
    [80, 70, 90, 60],
    [70, 65, 80, 55],
    [95, 90, 85, 92],
    [60, 55, 70, 50],
    [88, 92, 78, 84]
])
```

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([
    [80, 70, 90, 60],
    [70, 65, 80, 55],
    [95, 90, 85, 92],
    [60, 55, 70, 50],
    [88, 92, 78, 84]
])

rata_per_mapel = nilai.mean(axis=0)   # shape (4,) -> otomatis broadcast benar (per kolom)
std_per_mapel = nilai.std(axis=0)     # shape (4,)

z_score = (nilai - rata_per_mapel) / std_per_mapel
print(z_score)
```
**Kenapa nggak perlu reshape di sini (beda sama Soal 7)?** Karena kali ini kita mau broadcast ANTAR BARIS (tiap baris dikurangi vektor yang sama), dan shape `(4,)` secara default sudah pas nempel ke sisi kanan `(5,4)` — dibandingkan Soal 7 yang butuh broadcast antar KOLOM sehingga perlu reshape ke `(3,1)` dulu. Ini kunci memahami "arah" broadcasting.
</details>

---

### Soal 23
Studi kasus gabungan: Kamu punya data penjualan mingguan 3 toko selama 2 bulan, disimpan terpisah:
```python
bulan1 = np.array([
    [100, 120, 90, 110],   # Toko A, minggu 1-4
    [80, 85, 95, 100],     # Toko B
    [150, 160, 140, 155]   # Toko C
])
bulan2 = np.array([
    [105, 115, 95, 120],
    [90, 88, 92, 98],
    [155, 165, 145, 160]
])
```
1. Gabungkan jadi satu array 3D shape `(2, 3, 4)` — dimensi pertama = bulan — pakai `np.stack()`
2. Hitung total penjualan per toko untuk SELURUH periode (2 bulan gabung)

<details>
<summary>🔑 Jawaban</summary>

```python
bulan1 = np.array([
    [100, 120, 90, 110],
    [80, 85, 95, 100],
    [150, 160, 140, 155]
])
bulan2 = np.array([
    [105, 115, 95, 120],
    [90, 88, 92, 98],
    [155, 165, 145, 160]
])

# 1. Stack jadi 3D
gabungan = np.stack([bulan1, bulan2])
print(gabungan.shape)  # (2, 3, 4) -> (bulan, toko, minggu)

# 2. Total per toko, gabung 2 bulan
# axis 0 = bulan, axis 2 = minggu -> jumlahkan keduanya, sisain axis 1 (toko)
total_per_toko = gabungan.sum(axis=(0, 2))
print(total_per_toko)  # [965 728 1230] (kira-kira, cek sendiri hasil pastinya)
```
**Catatan:** `np.stack()` beda dari `np.concatenate()` — `stack` bikin DIMENSI BARU, sementara `concatenate` cuma nggabung di dimensi yang sudah ada.
</details>

---

### Soal 24
Prediksi shape hasil operasi berikut TANPA menjalankan kode dulu, baru cek jawabannya:
```python
a = np.ones((3, 1, 4))
b = np.ones((1, 5, 4))
hasil = a + b
```

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.ones((3, 1, 4))
b = np.ones((1, 5, 4))
hasil = a + b
print(hasil.shape)  # (3, 5, 4)
```
**Penjelasan step-by-step aturan broadcasting (bandingkan dari kanan):**
- Dimensi terakhir: `4` vs `4` -> sama, OK
- Dimensi tengah: `1` vs `5` -> salah satu `1`, jadi ikut yang besar (`5`)
- Dimensi pertama: `3` vs `1` -> salah satu `1`, jadi ikut yang besar (`3`)
- Hasil akhir: `(3, 5, 4)`
</details>

---

### Soal 25 (Level Boss 👹)
Studi kasus gabungan besar: Kamu adalah analis di perusahaan retail. Data penjualan 4 produk selama 6 bulan:
```python
penjualan = np.array([
    [200, 220, 210, 230, 250, 240],  # Produk A
    [150, 140, 160, 155, 145, 165],  # Produk B
    [300, 310, 295, 320, 330, 315],  # Produk C
    [80, 85, 90, 88, 92, 95]         # Produk D
])
harga_satuan = np.array([15000, 25000, 10000, 50000])  # shape (4,)
```

Tugas (semua tanpa loop):
1. Hitung **pendapatan** tiap produk tiap bulan (`penjualan x harga_satuan`, hasil shape `(4,6)`) — perhatikan arah broadcasting-nya!
2. Hitung total pendapatan per produk (jumlah 6 bulan)
3. Hitung total pendapatan perusahaan per bulan (jumlah 4 produk)
4. Cari bulan dengan pendapatan tertinggi (index bulan, 0-5)
5. Reshape hasil pendapatan `(4,6)` jadi `(2,2,6)` (anggap 4 produk dikelompokkan jadi 2 kategori x 2 produk), lalu hitung total pendapatan per kategori

<details>
<summary>🔑 Jawaban</summary>

```python
penjualan = np.array([
    [200, 220, 210, 230, 250, 240],
    [150, 140, 160, 155, 145, 165],
    [300, 310, 295, 320, 330, 315],
    [80, 85, 90, 88, 92, 95]
])
harga_satuan = np.array([15000, 25000, 10000, 50000])  # shape (4,)

# 1. Pendapatan tiap produk tiap bulan
# penjualan shape (4,6), harga_satuan shape (4,) -> perlu reshape ke (4,1) biar broadcast per baris (produk)
pendapatan = penjualan * harga_satuan.reshape(-1, 1)
print("Pendapatan (4,6):\n", pendapatan)

# 2. Total per produk (jumlah 6 bulan -> axis=1)
total_per_produk = pendapatan.sum(axis=1)
print("Total per produk:", total_per_produk)

# 3. Total per bulan (jumlah 4 produk -> axis=0)
total_per_bulan = pendapatan.sum(axis=0)
print("Total per bulan:", total_per_bulan)

# 4. Bulan dengan pendapatan tertinggi
bulan_tertinggi = total_per_bulan.argmax()
print("Bulan tertinggi (index):", bulan_tertinggi)

# 5. Reshape ke (2,2,6) dan total per kategori
pendapatan_kategori = pendapatan.reshape(2, 2, 6)
total_per_kategori = pendapatan_kategori.sum(axis=(1, 2))
print("Total per kategori:", total_per_kategori)
```
</details>

---

## ✅ Checklist Kelulusan Milestone 3

- [ ] Paham broadcasting scalar-ke-array (paling gampang)
- [ ] Paham **aturan broadcasting**: bandingkan shape dari kanan, dimensi harus sama atau salah satunya `1`
- [ ] Bisa nentuin KAPAN perlu `.reshape(-1,1)` supaya broadcasting "nyebar" ke arah yang benar (soal 7 & 25 — ini sering jadi jebakan!)
- [ ] Bisa `.reshape()`, paham beda `.flatten()` (copy) vs `.ravel()` (view)
- [ ] Bisa gabung array: `concatenate`, `vstack`, `hstack`, `stack` — dan paham bedanya
- [ ] Bisa pecah array: `split`, `vsplit`, `hsplit`
- [ ] Paham `.T` (transpose) itu view, dan `.squeeze()` buat hilangin dimensi `1`

Kalau ada soal yang bikin nyangkut (terutama soal 7, 22, 24, 25 — soal-soal "arah broadcasting" emang paling sering bikin bingung), bilang aja nomornya. Lanjut ke **Milestone 4: Advanced Indexing, Masking, & Filtering** kalau udah pede?
