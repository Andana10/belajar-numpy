# 📘 Milestone 4: Advanced Indexing, Masking, & Filtering

> Milestone ini adalah **jembatan paling langsung ke Pandas**. Hampir semua cara kamu "menyaring data" di Pandas (`df[df['umur'] > 25]`) itu turunan langsung dari konsep di sini. Kita bahas teorinya dulu tiap bagian, baru latihan.

---

## 📖 TEORI BAGIAN A: Boolean Masking

### Apa itu Boolean Mask?
Boolean mask adalah array berisi `True`/`False` yang **shape-nya sama** dengan array asli, dipakai buat "menyaring" elemen mana yang mau diambil.

Analoginya: bayangin kamu punya sebaris kelereng warna-warni, dan kamu punya "ayakan" yang cuma meloloskan kelereng merah. Ayakan itu ibarat boolean mask — bentuknya "menutupi" semua kelereng, tapi cuma yang kena kriteria (merah = `True`) yang lolos.

```python
import numpy as np
suhu = np.array([28, 31, 35, 22, 40, 19])
mask = suhu > 30        # ini boolean mask: [False True True False True False]
hasil = suhu[mask]      # [31 35 40] -> cuma yang True yang diambil
```

### Kenapa Ini Penting Banget?
Karena ini **PERSIS** cara kerja filter di Pandas:
```python
# NumPy
suhu[suhu > 30]

# Pandas (konsepnya identik!)
df[df['suhu'] > 30]
```
Kalau kamu udah jago di NumPy, filter Pandas bakal berasa "oh, ini kan yang tadi" — bukan konsep baru dari nol.

### Menggabungkan Kondisi
Di Python biasa kamu pakai `and`/`or`, tapi di NumPy **HARUS** pakai operator `&` (dan) dan `|` (atau), plus **wajib pakai kurung** di tiap kondisi:
```python
mask = (suhu > 20) & (suhu < 35)   # BENAR
mask = suhu > 20 & suhu < 35        # SALAH -> error atau hasil aneh!
```
Kenapa harus `&`/`|`? Karena `and`/`or` Python cuma bisa evaluasi SATU nilai boolean tunggal, sementara `&`/`|` di NumPy dirancang buat evaluasi elemen-per-elemen (elementwise) di seluruh array sekaligus.

---

## 🟢 LATIHAN BAGIAN A: Boolean Masking Dasar

### Soal 1
Diberikan `nilai = np.array([65, 45, 80, 90, 55, 70, 30])`. Buat mask untuk nilai **lulus** (≥60), lalu tampilkan nilai-nilai yang lulus.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([65, 45, 80, 90, 55, 70, 30])
mask_lulus = nilai >= 60
print(nilai[mask_lulus])  # [65 80 90 70]
```
</details>

---

### Soal 2
Dari array yang sama, hitung **berapa banyak** siswa yang tidak lulus (mask untuk nilai < 60, lalu `.sum()`).

<details>
<summary>🔑 Jawaban</summary>

```python
mask_tidak_lulus = nilai < 60
jumlah_tidak_lulus = mask_tidak_lulus.sum()
print(jumlah_tidak_lulus)  # 3
```
**Ingat:** `True` dihitung sebagai `1`, jadi `.sum()` pada array boolean = menghitung berapa banyak yang `True`.
</details>

---

### Soal 3
Diberikan `umur = np.array([17, 25, 16, 30, 22, 15, 40])`. Ambil semua umur yang **antara 18 dan 30** (inklusif), pakai kombinasi `&`.

<details>
<summary>🔑 Jawaban</summary>

```python
umur = np.array([17, 25, 16, 30, 22, 15, 40])
mask = (umur >= 18) & (umur <= 30)
print(umur[mask])  # [25 30 22]
```
</details>

---

### Soal 4
Dari array `umur` yang sama, ambil semua umur yang **DI LUAR** rentang 18-30 (di bawah 18 ATAU di atas 30), pakai `|`.

<details>
<summary>🔑 Jawaban</summary>

```python
mask = (umur < 18) | (umur > 30)
print(umur[mask])  # [17 16 15 40]
```
</details>

---

### Soal 5
Diberikan `nilai = np.array([65, 45, 80, 90, 55, 70, 30])`. Gunakan operator `~` (NOT) untuk membalik hasil mask "lulus" jadi mask "tidak lulus", tanpa menulis ulang kondisinya.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([65, 45, 80, 90, 55, 70, 30])
mask_lulus = nilai >= 60
mask_tidak_lulus = ~mask_lulus   # ~ membalik True jadi False dan sebaliknya
print(nilai[mask_tidak_lulus])  # [45 55 30]
```
</details>

---

## 📖 TEORI BAGIAN B: Modifikasi Data Lewat Mask

### Boolean Mask Bisa Dipakai untuk MENGUBAH Data
Selain buat "mengintip" data, mask juga bisa dipakai di sisi kiri (`=`) untuk **mengubah nilai** yang memenuhi kondisi tertentu — ini disebut **conditional assignment**.

```python
nilai = np.array([65, 45, 80, 90, 55])
nilai[nilai < 60] = 0   # semua yang < 60 diganti jadi 0
print(nilai)  # [65  0 80 90  0]
```
Ini beda dengan `np.where()` yang kamu pelajari di Milestone 2 — `np.where()` menghasilkan array BARU, sementara conditional assignment langsung **mengubah array aslinya (in-place)**.

### Kapan pakai yang mana?
- Pakai **conditional assignment** (`arr[mask] = nilai`) kalau kamu memang mau array aslinya berubah permanen.
- Pakai **`np.where()`** kalau kamu mau array baru tanpa mengubah yang asli (lebih aman untuk debugging).

---

## 🟡 LATIHAN BAGIAN B: Modifikasi via Mask

### Soal 6
Diberikan `stok = np.array([50, 0, 30, 0, 15, 0, 8])` (angka `0` berarti data hilang/error). Ganti semua nilai `0` menjadi `np.nan` (Not a Number) — ini teknik umum buat menandai "data hilang" sebelum analisis lanjut.

<details>
<summary>🔑 Jawaban</summary>

```python
stok = np.array([50, 0, 30, 0, 15, 0, 8], dtype=float)  # harus float supaya bisa nan
stok[stok == 0] = np.nan
print(stok)  # [50. nan 30. nan 15. nan  8.]
```
**Catatan:** `np.nan` cuma bisa disimpan di array bertipe `float`, bukan `int` — makanya kita set `dtype=float` dari awal.
</details>

---

### Soal 7
Diberikan `harga = np.array([15000, -5000, 22000, -1000, 30000])` (angka negatif = harga input salah/error). Ganti semua harga negatif jadi `0`.

<details>
<summary>🔑 Jawaban</summary>

```python
harga = np.array([15000, -5000, 22000, -1000, 30000])
harga[harga < 0] = 0
print(harga)  # [15000     0 22000     0 30000]
```
</details>

---

### Soal 8
Diberikan `nilai = np.array([55, 70, 88, 45, 92, 60, 78])`. Terapkan aturan: nilai di bawah 60 dianggap `0`, nilai 60 ke atas ditambah bonus `5` poin (maksimal 100). Gunakan DUA baris conditional assignment terpisah.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([55, 70, 88, 45, 92, 60, 78])
nilai[nilai < 60] = 0
nilai[nilai >= 60] += 5   # perhatikan: kondisi ini dicek ULANG setelah baris pertama
print(nilai)
# baris pertama ubah yg <60 jadi 0, baris kedua nambah yang asalnya >=60
# hasil: [ 0 75 93  0 97 65 83]
```
**Hati-hati:** Urutan operasi penting! Karena baris pertama mengubah beberapa nilai jadi `0`, baris kedua mengecek ulang kondisi `>= 60` dari data yang SUDAH berubah, bukan data asli. Untungnya di sini nggak masalah karena `0` tidak akan pernah `>= 60`.
</details>

---

## 📖 TEORI BAGIAN C: Fancy Indexing Lanjutan

### Mengambil Berdasarkan Banyak Kriteria Sekaligus
Fancy indexing bisa dikombinasikan dengan hasil dari fungsi pencarian seperti `np.where()` (tanpa argumen ke-2/ke-3) atau `np.argsort()` untuk kebutuhan yang lebih kompleks, misalnya "ambil 3 nilai tertinggi".

```python
nilai = np.array([65, 90, 45, 88, 70])
idx_urutan = np.argsort(nilai)          # index dari yang TERKECIL ke TERBESAR
print(idx_urutan)  # [2 0 4 3 1]

idx_3_tertinggi = idx_urutan[-3:]        # 3 index terakhir = 3 nilai terbesar
print(nilai[idx_3_tertinggi])            # [65 88 90]
```

### Indexing dengan Array 2D sebagai "Peta"
Kamu juga bisa pakai array index untuk 2 dimensi sekaligus — ambil pasangan (baris, kolom) tertentu:
```python
matriks = np.array([[1,2,3],[4,5,6],[7,8,9]])
baris = np.array([0, 1, 2])
kolom = np.array([2, 0, 1])
print(matriks[baris, kolom])  # [3 4 8] -> ambil (0,2), (1,0), (2,1)
```

---

## 🟠 LATIHAN BAGIAN C: Fancy Indexing Lanjutan

### Soal 9
Diberikan `nilai = np.array([72, 88, 65, 95, 58, 81, 90])`. Cari **3 nilai tertinggi** menggunakan `np.argsort()` (jangan pakai `.max()` berulang atau `sort()` manual).

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([72, 88, 65, 95, 58, 81, 90])
idx_urutan = np.argsort(nilai)
idx_3_tertinggi = idx_urutan[-3:]
print(nilai[idx_3_tertinggi])          # [88 90 95] (urutan naik)
print(nilai[idx_3_tertinggi][::-1])    # [95 90 88] (dibalik jadi turun)
```
</details>

---

### Soal 10
Diberikan `matriks = np.array([[10,20,30],[40,50,60],[70,80,90]])`. Ambil elemen di posisi (0,0), (1,1), (2,2) — yaitu diagonal utama — pakai fancy indexing dengan dua array index (baris dan kolom), BUKAN pakai `np.diagonal()`.

<details>
<summary>🔑 Jawaban</summary>

```python
matriks = np.array([[10,20,30],[40,50,60],[70,80,90]])
baris = np.array([0,1,2])
kolom = np.array([0,1,2])
print(matriks[baris, kolom])  # [10 50 90]
```
</details>

---

### Soal 11
Studi kasus: Diberikan nama siswa dan nilai mereka:
```python
siswa = np.array(["Ana", "Budi", "Citra", "Dedi", "Eka"])
nilai = np.array([75, 92, 60, 88, 55])
```
Tampilkan nama-nama siswa yang **rankingnya 3 besar** (nilai tertinggi), urut dari yang paling tinggi.

<details>
<summary>🔑 Jawaban</summary>

```python
siswa = np.array(["Ana", "Budi", "Citra", "Dedi", "Eka"])
nilai = np.array([75, 92, 60, 88, 55])

idx_urutan = np.argsort(nilai)[::-1]   # urutkan lalu balik (jadi turun)
top3_idx = idx_urutan[:3]
print("Ranking 3 besar:", siswa[top3_idx])   # ['Budi' 'Dedi' 'Ana']
print("Nilainya:", nilai[top3_idx])           # [92 88 75]
```
</details>

---

## 📖 TEORI BAGIAN D: np.isin(), np.any(), np.all()

### `np.isin()` — Cek Keanggotaan
Kalau kamu mau cek apakah elemen array ada di dalam sekumpulan nilai tertentu (mirip `in` di Python tapi buat banyak elemen sekaligus):
```python
kategori = np.array(["A", "B", "C", "D", "E"])
target = ["A", "C", "E"]
mask = np.isin(kategori, target)
print(mask)  # [ True False  True False  True]
```

### `np.any()` dan `np.all()` — Cek Kondisi Keseluruhan
- `np.any(kondisi)` → `True` kalau **ADA MINIMAL SATU** elemen yang memenuhi kondisi
- `np.all(kondisi)` → `True` kalau **SEMUA** elemen memenuhi kondisi

```python
nilai = np.array([70, 85, 45, 90])
print(np.any(nilai < 50))   # True -> ada minimal 1 yang < 50
print(np.all(nilai >= 60))  # False -> nggak semua >= 60
```
Ini SANGAT berguna buat validasi data cepat, misalnya: "apakah ada data yang hilang (NaN)?" atau "apakah semua data sudah bersih?"

---

## 🔴 LATIHAN BAGIAN D: isin, any, all

### Soal 12
Diberikan `kota = np.array(["Jakarta", "Bandung", "Surabaya", "Medan", "Semarang"])`. Cek mana saja yang termasuk dalam daftar `["Jakarta", "Semarang", "Malang"]` pakai `np.isin()`.

<details>
<summary>🔑 Jawaban</summary>

```python
kota = np.array(["Jakarta", "Bandung", "Surabaya", "Medan", "Semarang"])
target = ["Jakarta", "Semarang", "Malang"]
mask = np.isin(kota, target)
print(mask)          # [ True False False False  True]
print(kota[mask])    # ['Jakarta' 'Semarang']
```
</details>

---

### Soal 13
Diberikan `data = np.array([25, 30, np.nan, 40, np.nan, 55])`. Cek apakah **ADA** nilai yang hilang (`np.nan`) menggunakan `np.isnan()` + `np.any()`.

<details>
<summary>🔑 Jawaban</summary>

```python
data = np.array([25, 30, np.nan, 40, np.nan, 55])
ada_missing = np.any(np.isnan(data))
print(ada_missing)  # True
```
</details>

---

### Soal 14
Dari array `data` yang sama, hitung **berapa banyak** nilai yang hilang, lalu buat versi array yang HANYA berisi data valid (tanpa NaN) pakai `~np.isnan()`.

<details>
<summary>🔑 Jawaban</summary>

```python
jumlah_missing = np.isnan(data).sum()
print("Jumlah data hilang:", jumlah_missing)  # 2

data_bersih = data[~np.isnan(data)]
print("Data bersih:", data_bersih)  # [25. 30. 40. 55.]
```
**Ini teknik pembersihan data paling dasar** yang bakal terus kamu pakai — versi Pandas-nya adalah `.dropna()`.
</details>

---

### Soal 15
Diberikan dua array nilai ujian dari 2 kelas:
```python
kelas_a = np.array([70, 80, 90, 65])
kelas_b = np.array([75, 60, 85, 95])
```
Cek: apakah **SEMUA** siswa kelas A lulus (≥60)? Apakah **ADA** siswa kelas B yang dapat nilai sempurna (100)?

<details>
<summary>🔑 Jawaban</summary>

```python
kelas_a = np.array([70, 80, 90, 65])
kelas_b = np.array([75, 60, 85, 95])

semua_lulus_a = np.all(kelas_a >= 60)
print("Semua kelas A lulus?", semua_lulus_a)  # True

ada_sempurna_b = np.any(kelas_b == 100)
print("Ada nilai sempurna di kelas B?", ada_sempurna_b)  # False
```
</details>

---

## 🏆 BAGIAN E — Tantangan Bonus (Level Boss, Gabungan Semua Konsep)

### Soal 16
Studi kasus: Data transaksi e-commerce (nama produk, harga, jumlah terjual, kategori):
```python
produk = np.array(["Kaos", "Celana", "Topi", "Sepatu", "Jaket", "Kaos Kaki"])
harga = np.array([80000, 150000, 50000, 300000, 250000, 20000])
terjual = np.array([120, 45, 200, 30, 60, 500])
kategori = np.array(["Atasan", "Bawahan", "Aksesoris", "Sepatu", "Atasan", "Aksesoris"])
```
Tugas:
1. Hitung pendapatan tiap produk (`harga * terjual`)
2. Ambil semua produk dengan kategori **"Atasan"** ATAU **"Aksesoris"**, pakai `np.isin()`
3. Dari produk kategori itu, cari yang pendapatannya di atas rata-rata pendapatan SEMUA produk

<details>
<summary>🔑 Jawaban</summary>

```python
produk = np.array(["Kaos", "Celana", "Topi", "Sepatu", "Jaket", "Kaos Kaki"])
harga = np.array([80000, 150000, 50000, 300000, 250000, 20000])
terjual = np.array([120, 45, 200, 30, 60, 500])
kategori = np.array(["Atasan", "Bawahan", "Aksesoris", "Sepatu", "Atasan", "Aksesoris"])

# 1. Pendapatan tiap produk
pendapatan = harga * terjual
print("Pendapatan:", pendapatan)

# 2. Filter kategori Atasan/Aksesoris
mask_kategori = np.isin(kategori, ["Atasan", "Aksesoris"])
produk_terpilih = produk[mask_kategori]
pendapatan_terpilih = pendapatan[mask_kategori]
print("Produk terpilih:", produk_terpilih)

# 3. Yang di atas rata-rata SEMUA produk (bukan rata-rata yang sudah difilter!)
rata_rata_semua = pendapatan.mean()
mask_di_atas_rata = pendapatan_terpilih > rata_rata_semua
print("Di atas rata-rata semua produk:", produk_terpilih[mask_di_atas_rata])
```
</details>

---

### Soal 17
Diberikan matriks nilai ujian 6 siswa x 3 mapel. Cari siswa mana yang **LULUS SEMUA MAPEL** (nilai ≥ 60 di ketiga mapel), pakai `np.all(axis=1)`.

```python
nilai = np.array([
    [70, 65, 80],
    [55, 90, 75],
    [88, 92, 95],
    [45, 50, 40],
    [65, 60, 70],
    [90, 40, 85]
])
```

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([
    [70, 65, 80],
    [55, 90, 75],
    [88, 92, 95],
    [45, 50, 40],
    [65, 60, 70],
    [90, 40, 85]
])

mask_lulus_semua = np.all(nilai >= 60, axis=1)
print(mask_lulus_semua)  # [ True False  True False  True False]

idx_lulus = np.where(mask_lulus_semua)[0]
print("Index siswa lulus semua mapel:", idx_lulus)  # [0 2 4]
```
**Insight penting:** `axis=1` di sini artinya "cek SEPANJANG kolom (antar mapel) UNTUK TIAP baris (siswa)" — hasilnya satu nilai True/False per siswa.
</details>

---

### Soal 18 (Level Boss 👹)
Studi kasus gabungan besar: Data karyawan (nama, gaji, departemen, tahun bergabung):
```python
nama = np.array(["Andi", "Budi", "Citra", "Dedi", "Eka", "Fani", "Gita"])
gaji = np.array([5000000, 8000000, 6500000, 12000000, 4500000, 9000000, 7000000])
departemen = np.array(["IT", "Sales", "IT", "Manajemen", "HR", "Sales", "IT"])
tahun_gabung = np.array([2020, 2018, 2021, 2015, 2022, 2019, 2017])
```
Tugas:
1. Cari karyawan departemen **"IT"** yang gajinya **di atas rata-rata gaji IT saja** (bukan rata-rata semua karyawan)
2. Cari karyawan yang sudah bergabung **lebih dari 5 tahun** (asumsikan sekarang 2026) DAN gajinya **di bawah 8 juta** (kandidat kenaikan gaji)
3. Urutkan SEMUA nama karyawan berdasarkan gaji, dari tertinggi ke terendah

<details>
<summary>🔑 Jawaban</summary>

```python
nama = np.array(["Andi", "Budi", "Citra", "Dedi", "Eka", "Fani", "Gita"])
gaji = np.array([5000000, 8000000, 6500000, 12000000, 4500000, 9000000, 7000000])
departemen = np.array(["IT", "Sales", "IT", "Manajemen", "HR", "Sales", "IT"])
tahun_gabung = np.array([2020, 2018, 2021, 2015, 2022, 2019, 2017])

# 1. Karyawan IT di atas rata-rata gaji IT
mask_it = departemen == "IT"
gaji_it = gaji[mask_it]
rata_gaji_it = gaji_it.mean()
mask_it_atas_rata = mask_it & (gaji > rata_gaji_it)
print("IT di atas rata-rata IT:", nama[mask_it_atas_rata])

# 2. Lama kerja > 5 tahun DAN gaji < 8 juta
lama_kerja = 2026 - tahun_gabung
mask_kandidat = (lama_kerja > 5) & (gaji < 8000000)
print("Kandidat kenaikan gaji:", nama[mask_kandidat])

# 3. Urutkan semua nama berdasarkan gaji tertinggi ke terendah
idx_urutan = np.argsort(gaji)[::-1]
print("Ranking gaji (tertinggi dulu):", nama[idx_urutan])
print("Gajinya:", gaji[idx_urutan])
```
**Catatan soal 1:** Ini contoh nyata kenapa "rata-rata di dalam grup" beda dari "rata-rata keseluruhan" — kesalahan umum di analisis data adalah lupa filter dulu sebelum hitung rata-rata pembanding.
</details>

---

## ✅ Checklist Kelulusan Milestone 4

- [ ] Paham boolean mask dan kenapa harus pakai `&`/`|` (bukan `and`/`or`) dengan kurung di NumPy
- [ ] Bisa conditional assignment (`arr[mask] = nilai`) vs `np.where()` — dan tahu kapan pakai yang mana
- [ ] Bisa fancy indexing lanjutan dengan `np.argsort()` untuk ranking/top-N
- [ ] Bisa pakai `np.isin()` buat cek keanggotaan banyak nilai sekaligus
- [ ] Paham `np.any()` vs `np.all()`, terutama dengan parameter `axis`
- [ ] Bisa gabungkan beberapa mask sekaligus untuk filter kompleks (soal 16 & 18)
- [ ] Paham cara handle `np.nan` (`np.isnan()`, filter data hilang)

Semua konsep di milestone ini adalah **fondasi langsung** buat filtering di Pandas nanti (`df[mask]`, `df.isin()`, `df.dropna()`, `df.sort_values()`). Begitu kamu lulus checklist ini, kamu siap banget buat mulai Pandas kalau mau langsung loncat, atau lanjut ke **Milestone 5: Statistik & Linear Algebra** dulu kalau mau lebih lengkap.

Mau lanjut ke Milestone 5, atau langsung transisi ke Pandas?
