# 🏋️ Latihan Milestone 1: Fundamental NumPy & Array 1D/2D

> 25 soal, dari pemanasan sampai lumayan nantang. Kerjain berurutan, jangan loncat-loncat — tiap soal ngebangun pemahaman buat soal berikutnya. Coba dulu SENDIRI minimal 3-5 menit sebelum buka kunci jawaban!

---

## 🟢 BAGIAN A — Pemanasan: Membuat Array

### Soal 1
Buat array 1D dari list `[5, 10, 15, 20, 25]`, lalu cetak tipe datanya (`type()`) dan dtype-nya (`.dtype`).

<details>
<summary>🔑 Jawaban</summary>

```python
import numpy as np
arr = np.array([5, 10, 15, 20, 25])
print(type(arr))   # <class 'numpy.ndarray'>
print(arr.dtype)    # int64 (tergantung OS, bisa int32 di Windows)
```
</details>

---

### Soal 2
Buat array 1D berisi angka **0 sampai 9** tanpa menulis manual satu-satu (pakai `np.arange()`).

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
```
</details>

---

### Soal 3
Buat array berisi 5 angka yang **merata (evenly spaced)** antara 0 dan 1 (pakai `np.linspace()`).

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.linspace(0, 1, 5)
print(arr)  # [0.   0.25 0.5  0.75 1.  ]
```
</details>

---

### Soal 4
Buat array 3x3 isinya semua angka **0** (pakai `np.zeros()`), lalu array 2x4 isinya semua angka **1** (pakai `np.ones()`).

<details>
<summary>🔑 Jawaban</summary>

```python
nol = np.zeros((3, 3))
satu = np.ones((2, 4))
print(nol)
print(satu)
```
</details>

---

### Soal 5
Buat array identitas (identity matrix) ukuran 4x4 pakai `np.eye()`.

<details>
<summary>🔑 Jawaban</summary>

```python
identitas = np.eye(4)
print(identitas)
# Diagonal utama isinya 1, sisanya 0
```
</details>

---

## 🟡 BAGIAN B — Memahami Shape, Dimensi, & Dtype

### Soal 6
Diberikan array berikut:
```python
data = np.array([[1, 2, 3], [4, 5, 6]])
```
Tanpa menjalankan kode, coba tebak: berapa `.ndim`, `.shape`, dan `.size`-nya? Baru cek jawabanmu dengan kode.

<details>
<summary>🔑 Jawaban</summary>

```python
print(data.ndim)   # 2 -> dua dimensi (baris & kolom)
print(data.shape)  # (2, 3) -> 2 baris, 3 kolom
print(data.size)   # 6 -> total elemen (2 x 3)
```
</details>

---

### Soal 7
Buat array `nilai = np.array([80, 90.5, 70])`. Kenapa dtype-nya jadi `float64`, padahal ada angka `80` dan `70` yang integer?

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([80, 90.5, 70])
print(nilai.dtype)  # float64
```
**Penjelasan:** Ingat analogi "rak telur" — semua elemen array HARUS punya tipe yang sama. Karena ada satu angka desimal (`90.5`), NumPy otomatis "upgrade" semua elemen lain jadi float biar konsisten. Ini disebut **type coercion / upcasting**.
</details>

---

### Soal 8
Paksa sebuah array `np.array([1, 2, 3])` (defaultnya int) supaya dtype-nya jadi `float32` sejak awal dibuat.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([1, 2, 3], dtype=np.float32)
print(arr.dtype)  # float32
print(arr)         # [1. 2. 3.]
```
</details>

---

### Soal 9
Buat array 3D dengan shape `(2, 3, 4)` isinya angka acak antara 0-1 (pakai `np.random.rand()`), lalu cetak `.ndim` dan `.shape`-nya. Coba bayangkan ini representasi apa (hint: kayak 2 "lembar" tabel 3x4).

<details>
<summary>🔑 Jawaban</summary>

```python
arr3d = np.random.rand(2, 3, 4)
print(arr3d.ndim)   # 3
print(arr3d.shape)  # (2, 3, 4)
```
**Penjelasan:** Bayangin ini 2 buah tabel (matriks), masing-masing tabel punya 3 baris dan 4 kolom. Konsep ini penting nanti pas kamu belajar data gambar berwarna (RGB) atau data time-series multi-fitur.
</details>

---

### Soal 10
Diberikan `arr = np.array([1, 2, 3])`. Berapa ukuran memori total array ini dalam byte? (Gunakan `.itemsize` dan `.nbytes`).

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([1, 2, 3])
print(arr.itemsize)  # 8 (byte per elemen, karena int64)
print(arr.nbytes)    # 24 (3 elemen x 8 byte)
```
</details>

---

## 🟠 BAGIAN C — Operasi Dasar & Vectorization

### Soal 11
Diberikan `harga = np.array([10000, 25000, 5000, 40000])`. Hitung harga setelah diskon 15% untuk SEMUA item sekaligus (tanpa loop!).

<details>
<summary>🔑 Jawaban</summary>

```python
harga = np.array([10000, 25000, 5000, 40000])
harga_diskon = harga * 0.85
print(harga_diskon)  # [ 8500. 21250.  4250. 34000.]
```
</details>

---

### Soal 12
Diberikan dua array nilai ujian:
```python
uts = np.array([80, 70, 90])
uas = np.array([85, 75, 95])
```
Hitung **nilai akhir** dengan bobot UTS 40% dan UAS 60%, langsung dalam satu baris kode (tanpa loop).

<details>
<summary>🔑 Jawaban</summary>

```python
uts = np.array([80, 70, 90])
uas = np.array([85, 75, 95])
nilai_akhir = uts * 0.4 + uas * 0.6
print(nilai_akhir)  # [83. 73. 93.]
```
</details>

---

### Soal 13
Buktikan kenapa vectorization NumPy lebih cepat dari loop Python biasa. Buat array besar (1 juta elemen), lalu bandingkan waktu kuadratkan semua elemen pakai **loop `for`** vs **operasi NumPy langsung** (pakai modul `time`).

<details>
<summary>🔑 Jawaban</summary>

```python
import time

n = 1_000_000
data = list(range(n))
data_np = np.arange(n)

# Cara 1: Loop Python biasa
start = time.time()
hasil_loop = [x**2 for x in data]
print("Loop:", time.time() - start, "detik")

# Cara 2: Vectorization NumPy
start = time.time()
hasil_np = data_np ** 2
print("NumPy:", time.time() - start, "detik")
```
**Penjelasan:** Biasanya NumPy bisa **10-100x lebih cepat**. Ini karena NumPy memproses data di level C (bukan interpreter Python) dan memanfaatkan bahwa semua elemen tipenya sama (homogen).
</details>

---

### Soal 14
Diberikan `suhu_celcius = np.array([0, 20, 37, 100])`. Konversi semua nilai ke Fahrenheit dengan rumus `F = C * 9/5 + 32`, dalam satu baris.

<details>
<summary>🔑 Jawaban</summary>

```python
suhu_celcius = np.array([0, 20, 37, 100])
suhu_f = suhu_celcius * 9/5 + 32
print(suhu_f)  # [ 32.  68.  98.6 212. ]
```
</details>

---

### Soal 15
Diberikan `a = np.array([1, 2, 3])` dan `b = np.array([4, 5, 6])`. Hitung: penjumlahan, pengurangan, perkalian elemen-per-elemen, dan pembagian — semuanya elementwise (bukan operasi matriks).

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # [ 4 10 18]
print(a / b)  # [0.25 0.4  0.5 ]
```
</details>

---

## 🔴 BAGIAN D — Array 2D & Studi Kasus Mini

### Soal 16
Buat array 2D `nilai_kelas` berisi nilai 4 siswa untuk 3 mata pelajaran (isi bebas, angka 0-100). Cetak `.shape`, lalu hitung **rata-rata keseluruhan** pakai `.mean()`.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai_kelas = np.array([
    [80, 75, 90],
    [70, 85, 88],
    [95, 60, 77],
    [82, 91, 73]
])
print(nilai_kelas.shape)  # (4, 3)
print(nilai_kelas.mean())  # rata-rata semua 48 nilai (contoh: ~80.5)
```
</details>

---

### Soal 17
Dari array `nilai_kelas` di soal 16, hitung **rata-rata per siswa** (per baris) dan **rata-rata per mata pelajaran** (per kolom) — pakai parameter `axis`.

<details>
<summary>🔑 Jawaban</summary>

```python
rata_per_siswa = nilai_kelas.mean(axis=1)   # axis=1 -> nyebrangin kolom, hasil per baris
rata_per_mapel = nilai_kelas.mean(axis=0)   # axis=0 -> nyebrangin baris, hasil per kolom
print("Rata-rata per siswa:", rata_per_siswa)
print("Rata-rata per mapel:", rata_per_mapel)
```
**Tips ingat axis:** `axis=0` itu arah "ke bawah" (antar baris), `axis=1` itu arah "ke samping" (antar kolom). Kalau bingung, bayangin axis itu dimensi yang "dihancurkan"/diringkas.
</details>

---

### Soal 18
Buat array 2D ukuran 5x5 isinya angka 1-25 berurutan (pakai kombinasi `np.arange()` dan `.reshape()`).

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(1, 26).reshape(5, 5)
print(arr)
```
</details>

---

### Soal 19
Dari array 5x5 di soal 18, cari nilai **maksimum**, **minimum**, dan **jumlah total** semua elemen.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.arange(1, 26).reshape(5, 5)
print(arr.max())   # 25
print(arr.min())   # 1
print(arr.sum())   # 325
```
</details>

---

### Soal 20
Studi kasus: Kamu punya data suhu selama seminggu (7 hari) untuk 3 kota berbeda. Buat array 3x7 (3 baris = kota, 7 kolom = hari) dengan angka acak antara 20-35 derajat (pakai `np.random.randint()`). Lalu cari kota mana yang punya **rata-rata suhu tertinggi**.

<details>
<summary>🔑 Jawaban</summary>

```python
np.random.seed(42)  # biar hasilnya konsisten tiap dijalankan
suhu_mingguan = np.random.randint(20, 36, size=(3, 7))
kota = ["Jakarta", "Bandung", "Surabaya"]

rata_per_kota = suhu_mingguan.mean(axis=1)
print("Rata-rata suhu per kota:", rata_per_kota)

idx_tertinggi = rata_per_kota.argmax()
print(f"Kota dengan rata-rata suhu tertinggi: {kota[idx_tertinggi]}")
```
**Catatan:** `np.random.seed(42)` dipakai supaya angka random-nya selalu sama tiap kali kode dijalankan — penting banget buat keperluan belajar/debugging biar hasilnya bisa direproduksi.
</details>

---

## 🏆 BAGIAN E — Tantangan Bonus (Level Kepercayaan Diri)

### Soal 21
Buat array 1D berisi 20 angka acak integer antara 1-100. Hitung: mean, median (`np.median()`), standar deviasi (`.std()`), dan nilai unik yang muncul (`np.unique()`).

<details>
<summary>🔑 Jawaban</summary>

```python
np.random.seed(1)
data = np.random.randint(1, 101, size=20)
print("Data:", data)
print("Mean:", data.mean())
print("Median:", np.median(data))
print("Std Dev:", data.std())
print("Unique:", np.unique(data))
```
</details>

---

### Soal 22
Diberikan array `harga_produk = np.array([15000, 22000, 8000, 30000, 12000])`. Tanpa pakai loop, cetak produk ke berapa (index) yang harganya paling mahal, dan berapa harganya.

<details>
<summary>🔑 Jawaban</summary>

```python
harga_produk = np.array([15000, 22000, 8000, 30000, 12000])
idx_termahal = harga_produk.argmax()
print(f"Produk termahal adalah produk ke-{idx_termahal} dengan harga {harga_produk[idx_termahal]}")
```
</details>

---

### Soal 23
Buat 2 array: `a = np.array([1, 2, 3])` dan `b = np.array([1, 2, 3])`. Cek apakah keduanya **identik** menggunakan `np.array_equal()`. Lalu ubah satu elemen di `b` dan cek lagi.

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
print(np.array_equal(a, b))  # True

b[0] = 99
print(np.array_equal(a, b))  # False
```
**Kenapa nggak pakai `a == b` biasa?** Karena `a == b` akan menghasilkan array boolean elementwise `[True, True, True]`, bukan satu nilai True/False tunggal. `np.array_equal()` yang tepat buat cek kesamaan keseluruhan array.
</details>

---

### Soal 24
Diberikan matriks nilai `nilai = np.array([[90, 85], [70, 60], [88, 92]])` (kolom pertama = nilai teori, kolom kedua = nilai praktik). Hitung nilai akhir per siswa dengan bobot **40% teori + 60% praktik**, tanpa loop.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([[90, 85], [70, 60], [88, 92]])
teori = nilai[:, 0]     # ambil semua baris, kolom index 0
praktik = nilai[:, 1]   # ambil semua baris, kolom index 1

nilai_akhir = teori * 0.4 + praktik * 0.6
print(nilai_akhir)  # [87.  64.  90.4]
```
**Catatan:** Ini sekilas "bocoran" indexing yang akan kamu pelajari detail di Milestone 2 — `[:, 0]` artinya "semua baris, kolom ke-0".
</details>

---

### Soal 25 (Level Boss 👹)
Studi kasus gabungan: Kamu adalah analis di sebuah toko online. Diberikan data penjualan 5 produk selama 4 minggu:

```python
penjualan = np.array([
    [120, 135, 150, 110],  # Produk A
    [80,  95,  70,  100],  # Produk B
    [200, 180, 220, 210],  # Produk C
    [50,  60,  55,  65],   # Produk D
    [300, 310, 290, 320]   # Produk E
])
```

Tugas:
1. Hitung total penjualan per produk (per baris)
2. Hitung total penjualan per minggu (per kolom)
3. Cari produk dengan total penjualan tertinggi
4. Hitung rata-rata penjualan keseluruhan toko

<details>
<summary>🔑 Jawaban</summary>

```python
penjualan = np.array([
    [120, 135, 150, 110],
    [80,  95,  70,  100],
    [200, 180, 220, 210],
    [50,  60,  55,  65],
    [300, 310, 290, 320]
])
produk = ["A", "B", "C", "D", "E"]

# 1. Total per produk
total_per_produk = penjualan.sum(axis=1)
print("Total per produk:", total_per_produk)

# 2. Total per minggu
total_per_minggu = penjualan.sum(axis=0)
print("Total per minggu:", total_per_minggu)

# 3. Produk dengan total tertinggi
idx_terlaris = total_per_produk.argmax()
print(f"Produk terlaris: Produk {produk[idx_terlaris]} dengan total {total_per_produk[idx_terlaris]}")

# 4. Rata-rata keseluruhan
print("Rata-rata penjualan toko:", penjualan.mean())
```
</details>

---

## ✅ Checklist Kelulusan Milestone 1

Kalau kamu sudah bisa jawab semua soal di atas **tanpa buka kunci jawaban duluan**, kamu resmi lulus Milestone 1! Cek pemahamanmu:

- [ ] Bisa bikin array pakai `np.array()`, `np.arange()`, `np.linspace()`, `np.zeros()`, `np.ones()`
- [ ] Paham beda `.ndim`, `.shape`, `.size`, `.dtype`
- [ ] Paham kenapa array itu harus homogen (tipe data seragam)
- [ ] Bisa operasi elementwise tanpa loop (vectorization)
- [ ] Paham konsep `axis=0` vs `axis=1` di array 2D
- [ ] Bisa pakai fungsi statistik dasar: `.mean()`, `.sum()`, `.max()`, `.min()`, `.std()`

Kalau ada yang masih bingung, bilang aja bagian mana — nanti aku jelasin ulang pakai analogi lain. Siap lanjut ke **Milestone 2: Indexing, Slicing, & Vectorization**?
