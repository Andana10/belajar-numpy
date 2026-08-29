# 🏋️ Latihan Milestone 2: Indexing, Slicing, & Vectorization

> 25 soal. Fokus milestone ini: **ambil data spesifik dari array tanpa loop**. Analoginya, kalau Milestone 1 ngajarin kamu "bikin rak buku", Milestone 2 ngajarin kamu "cara ambil buku tertentu dari rak itu secepat mungkin" — baik satu buku, sebaris buku, atau buku-buku dengan kriteria tertentu.

Kerjain berurutan, coba sendiri dulu minimal 3-5 menit sebelum buka kunci jawaban!

---

## 🟢 BAGIAN A — Indexing Dasar (1D)

### Soal 1
Diberikan `arr = np.array([10, 20, 30, 40, 50])`. Ambil elemen pertama dan elemen terakhir **tanpa hardcode angka index terakhir** (pakai index negatif).

<details>
<summary>🔑 Jawaban</summary>

```python
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])   # 10 -> elemen pertama
print(arr[-1])  # 50 -> elemen terakhir, index negatif nggak perlu tahu panjang array
```
</details>

---

### Soal 2
Dari array yang sama, ubah nilai elemen ke-3 (index 2) menjadi `99`.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([10, 20, 30, 40, 50])
arr[2] = 99
print(arr)  # [10 20 99 40 50]
```
</details>

---

### Soal 3
Diberikan `nilai = np.array([65, 70, 55, 80, 90, 45, 100])`. Ambil 3 elemen pertama, lalu ambil 3 elemen terakhir — masing-masing pakai slicing (bukan indexing satu-satu).

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([65, 70, 55, 80, 90, 45, 100])
print(nilai[:3])   # [65 70 55] -> dari awal sampai index 3 (exclusive)
print(nilai[-3:])  # [90 45 100] -> 3 dari belakang sampai akhir
```
</details>

---

### Soal 4
Dari array `nilai` di soal 3, ambil elemen dengan **step 2** (index 0, 2, 4, 6, ...).

<details>
<summary>🔑 Jawaban</summary>

```python
print(nilai[::2])  # [65 55 90 100] -> format slicing [start:stop:step]
```
</details>

---

### Soal 5
Balik urutan array `nilai` (dari belakang ke depan) **dalam satu baris**, tanpa fungsi `reversed()` atau loop.

<details>
<summary>🔑 Jawaban</summary>

```python
print(nilai[::-1])  # [100  45  90  80  55  70  65]
```
**Trik:** `[::-1]` artinya "mulai dari akhir, ke awal, step -1". Ini salah satu trik slicing NumPy yang paling sering dipakai.
</details>

---

## 🟡 BAGIAN B — Indexing & Slicing pada Array 2D

### Soal 6
Diberikan:
```python
matriks = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```
Ambil elemen di baris ke-1, kolom ke-2 (ingat: index mulai dari 0) dengan **dua cara**: `matriks[1][2]` dan `matriks[1, 2]`. Kenapa cara kedua lebih disarankan di NumPy?

<details>
<summary>🔑 Jawaban</summary>

```python
matriks = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matriks[1][2])   # 6
print(matriks[1, 2])   # 6 (sama hasilnya)
```
**Penjelasan:** `matriks[1][2]` sebenarnya bikin array sementara dulu dari baris 1 (`[4,5,6]`), baru ambil index 2 dari situ — dua langkah tersembunyi. Sementara `matriks[1, 2]` langsung "loncat" ke posisi itu di memori — lebih efisien, apalagi buat array besar.
</details>

---

### Soal 7
Dari `matriks` di soal 6, ambil **seluruh baris pertama** dan **seluruh kolom pertama**.

<details>
<summary>🔑 Jawaban</summary>

```python
print(matriks[0, :])   # [1 2 3] -> baris pertama, semua kolom
print(matriks[:, 0])   # [1 4 7] -> semua baris, kolom pertama
```
</details>

---

### Soal 8
Dari `matriks` yang sama, ambil **sub-matriks 2x2** di pojok kiri atas (baris 0-1, kolom 0-1).

<details>
<summary>🔑 Jawaban</summary>

```python
print(matriks[0:2, 0:2])
# [[1 2]
#  [4 5]]
```
</details>

---

### Soal 9
Ambil kolom terakhir dan baris terakhir dari `matriks`, pakai index negatif.

<details>
<summary>🔑 Jawaban</summary>

```python
print(matriks[:, -1])   # [3 6 9] -> kolom terakhir
print(matriks[-1, :])   # [7 8 9] -> baris terakhir
```
</details>

---

### Soal 10
Studi kasus: Diberikan data nilai 5 siswa untuk 4 mata pelajaran (Matematika, Fisika, Kimia, Biologi):
```python
nilai_siswa = np.array([
    [80, 75, 90, 85],
    [70, 65, 80, 75],
    [95, 90, 85, 92],
    [60, 55, 70, 65],
    [88, 92, 78, 84]
])
```
Ambil semua nilai **Fisika** (kolom index 1) untuk semua siswa, lalu ambil semua nilai siswa ke-3 (index 2) untuk semua mata pelajaran.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai_fisika = nilai_siswa[:, 1]
print("Nilai Fisika semua siswa:", nilai_fisika)  # [75 65 90 55 92]

nilai_siswa_ke3 = nilai_siswa[2, :]
print("Nilai siswa ke-3:", nilai_siswa_ke3)  # [95 90 85 92]
```
</details>

---

## 🟠 BAGIAN C — Copy vs View (Konsep Krusial!)

### Soal 11
Diberikan `a = np.array([1, 2, 3, 4, 5])`. Buat `b = a[1:4]` (hasil slicing), lalu ubah `b[0] = 99`. Cetak `a` — apakah ikut berubah? Kenapa?

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 99
print(a)  # [ 1 99  3  4  5] -> IKUT BERUBAH!
```
**Penjelasan PENTING:** Slicing di NumPy menghasilkan **view**, bukan copy baru. `b` itu cuma "jendela" yang nunjuk ke memori yang sama dengan `a`. Ini beda banget sama Python list biasa! Ini salah satu jebakan paling umum yang bikin pemula bingung kenapa data "tiba-tiba berubah sendiri".
</details>

---

### Soal 12
Ulangi soal 11, tapi kali ini gunakan `.copy()` supaya `b` benar-benar independen dari `a`. Buktikan `a` tidak berubah.

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.array([1, 2, 3, 4, 5])
b = a[1:4].copy()
b[0] = 99
print(a)  # [1 2 3 4 5] -> TIDAK berubah
print(b)  # [99  3  4]
```
**Aturan main:** Kalau kamu mau modifikasi hasil slicing tanpa mempengaruhi array asli, SELALU pakai `.copy()`.
</details>

---

### Soal 13
Cek apakah dua array berbagi memori yang sama menggunakan atribut `.base`. Buktikan bahwa hasil slicing (`view`) punya `.base` yang menunjuk ke array asli, sementara hasil `.copy()` punya `.base` bernilai `None`.

<details>
<summary>🔑 Jawaban</summary>

```python
a = np.array([1, 2, 3, 4, 5])
view = a[1:4]
copy = a[1:4].copy()

print(view.base is a)  # True -> view "menumpang" di memori a
print(copy.base is None)  # True -> copy punya memori sendiri
```
</details>

---

## 🔴 BAGIAN D — Vectorization Lanjutan

### Soal 14
Diberikan `harga = np.array([15000, 22000, 8000, 30000, 12000])` dan `stok = np.array([10, 5, 20, 3, 15])`. Hitung **total nilai inventaris** (harga × stok, dijumlahkan semua) dalam satu ekspresi, tanpa loop.

<details>
<summary>🔑 Jawaban</summary>

```python
harga = np.array([15000, 22000, 8000, 30000, 12000])
stok = np.array([10, 5, 20, 3, 15])

total_nilai = (harga * stok).sum()
print(total_nilai)  # 150000+110000+160000+90000+180000 = 690000
```
</details>

---

### Soal 15
Diberikan `suhu = np.array([15, 22, 28, 33, 19, 25, 30])` (suhu 7 hari dalam Celsius). Tanpa loop, ubah SEMUA suhu di atas 30°C menjadi tepat `30` (capping/clipping nilai). Gunakan `np.where()`.

<details>
<summary>🔑 Jawaban</summary>

```python
suhu = np.array([15, 22, 28, 33, 19, 25, 30])
suhu_capped = np.where(suhu > 30, 30, suhu)
print(suhu_capped)  # [15 22 28 30 19 25 30]
```
**Cara baca `np.where(kondisi, nilai_jika_true, nilai_jika_false)`:** "Kalau suhu > 30, ganti jadi 30, kalau nggak, biarin nilai aslinya."
</details>

---

### Soal 16
Ulangi soal 15 tapi pakai fungsi built-in yang lebih ringkas: `np.clip()`. Kali ini batasi suhu ke rentang **18-30°C** (di bawah 18 jadi 18, di atas 30 jadi 30).

<details>
<summary>🔑 Jawaban</summary>

```python
suhu_clipped = np.clip(suhu, 18, 30)
print(suhu_clipped)  # [18 22 28 30 19 25 30]
```
</details>

---

### Soal 17
Diberikan dua array nama produk (index sejajar) dan harga:
```python
produk = np.array(["Sabun", "Shampo", "Pasta Gigi", "Sikat Gigi"])
harga = np.array([5000, 25000, 8000, 12000])
```
Cari nama produk dengan harga tertinggi menggunakan kombinasi `.argmax()` dan indexing (tanpa loop atau manual mapping).

<details>
<summary>🔑 Jawaban</summary>

```python
produk = np.array(["Sabun", "Shampo", "Pasta Gigi", "Sikat Gigi"])
harga = np.array([5000, 25000, 8000, 12000])

idx_termahal = harga.argmax()
print(produk[idx_termahal])  # Shampo
```
**Insight:** `.argmax()` di array `harga` menghasilkan index, dan karena `produk` dan `harga` "sejajar" (index sama = data terkait), kita bisa langsung "loncat" ke nama produknya lewat index yang sama.
</details>

---

### Soal 18
Diberikan `nilai = np.array([55, 70, 88, 45, 92, 60, 78])`. Tanpa loop, ubah semua nilai **di bawah 60** (nilai tidak lulus) menjadi `0`, sisanya biarkan apa adanya.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([55, 70, 88, 45, 92, 60, 78])
nilai_final = np.where(nilai < 60, 0, nilai)
print(nilai_final)  # [ 0 70 88  0 92 60 78]
```
</details>

---

## 🟣 BAGIAN E — Fancy Indexing (Preview Boolean & List Indexing)

> Ini teknik yang bakal kamu perdalam lagi di Milestone 4, tapi dasarnya penting dikenalin di sini karena masih "keluarga" indexing.

### Soal 19
Diberikan `arr = np.array([100, 200, 300, 400, 500])`. Ambil elemen index **0, 2, dan 4** sekaligus dengan cara memasukkan **list index** ke dalam kurung siku (bukan slicing biasa).

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([100, 200, 300, 400, 500])
print(arr[[0, 2, 4]])  # [100 300 500]
```
**Ini disebut fancy indexing** — beda dari slicing biasa, hasilnya SELALU copy (bukan view), dan kamu bisa ambil elemen dengan urutan/kombinasi bebas, bahkan bisa duplikat index.
</details>

---

### Soal 20
Buktikan bahwa fancy indexing menghasilkan **copy**, bukan view (beda dengan slicing biasa di soal 11). Ambil `b = arr[[0, 2, 4]]`, ubah `b[0] = 999`, lalu cek apakah `arr` ikut berubah.

<details>
<summary>🔑 Jawaban</summary>

```python
arr = np.array([100, 200, 300, 400, 500])
b = arr[[0, 2, 4]]
b[0] = 999
print(arr)  # [100 200 300 400 500] -> TIDAK berubah, karena fancy indexing = copy
```
</details>

---

### Soal 21
Diberikan `suhu = np.array([28, 31, 35, 22, 40, 19])`. Gunakan boolean mask untuk ambil semua suhu yang **lebih besar dari 25**, lalu hitung berapa banyak hari yang suhunya di atas 25 (pakai `.sum()` pada hasil mask boolean).

<details>
<summary>🔑 Jawaban</summary>

```python
suhu = np.array([28, 31, 35, 22, 40, 19])
mask = suhu > 25
print(suhu[mask])       # [28 31 35 40]
print(mask.sum())        # 4 -> True dihitung sebagai 1, False sebagai 0
```
**Insight menarik:** Di NumPy, `True` = `1` dan `False` = `0` kalau dijumlahkan. Ini trik umum buat "menghitung berapa banyak elemen yang memenuhi kondisi tertentu".
</details>

---

## 🏆 BAGIAN F — Tantangan Bonus (Level Boss)

### Soal 22
Studi kasus: Kamu punya data transaksi harian sebuah toko selama 10 hari:
```python
transaksi = np.array([1200000, 850000, 0, 2100000, 950000, 0, 1750000, 600000, 0, 3000000])
```
(Angka `0` berarti toko tutup di hari itu.)

Tugas:
1. Ambil hanya hari-hari toko **buka** (transaksi != 0) pakai boolean mask
2. Hitung rata-rata transaksi HANYA di hari toko buka (bukan rata-rata dari semua 10 hari)
3. Cari index hari dengan transaksi tertinggi

<details>
<summary>🔑 Jawaban</summary>

```python
transaksi = np.array([1200000, 850000, 0, 2100000, 950000, 0, 1750000, 600000, 0, 3000000])

# 1. Hari buka
mask_buka = transaksi != 0
hari_buka = transaksi[mask_buka]
print("Transaksi hari buka:", hari_buka)

# 2. Rata-rata hari buka saja
print("Rata-rata (hari buka):", hari_buka.mean())
# Beda jauh sama transaksi.mean() yang bakal ke-drag turun karena ada nilai 0

# 3. Index hari dengan transaksi tertinggi (dari data ASLI, bukan yang sudah difilter)
idx_tertinggi = transaksi.argmax()
print(f"Transaksi tertinggi di hari ke-{idx_tertinggi + 1} sebesar {transaksi[idx_tertinggi]}")
```
</details>

---

### Soal 23
Diberikan matriks nilai ujian 5 siswa x 3 mapel:
```python
nilai = np.array([
    [80, 90, 70],
    [55, 60, 50],
    [95, 88, 92],
    [40, 45, 38],
    [75, 80, 82]
])
```
Tanpa loop: cari siswa mana saja (index-nya) yang **rata-rata nilainya di bawah 60** (dianggap perlu remedial).

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([
    [80, 90, 70],
    [55, 60, 50],
    [95, 88, 92],
    [40, 45, 38],
    [75, 80, 82]
])

rata_per_siswa = nilai.mean(axis=1)
print("Rata-rata per siswa:", rata_per_siswa)

mask_remedial = rata_per_siswa < 60
idx_remedial = np.where(mask_remedial)[0]
print("Siswa yang perlu remedial (index):", idx_remedial)  # [1 3]
```
**Catatan:** `np.where(kondisi)` tanpa argumen kedua/ketiga akan mengembalikan **index** tempat kondisi bernilai True — beda fungsi dengan `np.where(kondisi, a, b)` yang kamu pakai di soal 15-16.
</details>

---

### Soal 24
Diberikan array 2D representasi papan tic-tac-toe:
```python
board = np.array([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
])
```
Ambil **diagonal utama** (kiri-atas ke kanan-bawah) menggunakan `np.diagonal()`, dan hitung berapa banyak "X" ada di diagonal tersebut.

<details>
<summary>🔑 Jawaban</summary>

```python
board = np.array([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "O", "X"]
])

diag = np.diagonal(board)
print("Diagonal utama:", diag)  # ['X' 'X' 'X']
jumlah_x = (diag == "X").sum()
print("Jumlah X di diagonal:", jumlah_x)  # 3 -> berarti X menang!
```
</details>

---

### Soal 25 (Level Boss 👹)
Studi kasus gabungan: Data suhu harian 4 kota selama 7 hari:
```python
suhu = np.array([
    [30, 32, 31, 29, 33, 34, 30],  # Jakarta
    [22, 21, 23, 20, 22, 24, 21],  # Bandung
    [28, 29, 27, 30, 28, 26, 29],  # Surabaya
    [18, 17, 19, 16, 18, 20, 17]   # Malang
])
kota = np.array(["Jakarta", "Bandung", "Surabaya", "Malang"])
```

Tugas (semua tanpa loop):
1. Ambil semua data suhu untuk kota **Bandung** (pakai boolean mask pada array `kota`, bukan hardcode index)
2. Cari hari ke berapa (index 0-6) suhu di Jakarta paling panas
3. Cari kota mana yang suhu rata-ratanya **di bawah 25°C**
4. Ganti semua suhu Malang yang di bawah 17°C jadi tepat 17°C (pakai `np.clip` atau `np.where`)

<details>
<summary>🔑 Jawaban</summary>

```python
suhu = np.array([
    [30, 32, 31, 29, 33, 34, 30],
    [22, 21, 23, 20, 22, 24, 21],
    [28, 29, 27, 30, 28, 26, 29],
    [18, 17, 19, 16, 18, 20, 17]
])
kota = np.array(["Jakarta", "Bandung", "Surabaya", "Malang"])

# 1. Data suhu Bandung pakai boolean mask di array kota
mask_bandung = kota == "Bandung"
suhu_bandung = suhu[mask_bandung]
print("Suhu Bandung:", suhu_bandung)  # [[22 21 23 20 22 24 21]]

# 2. Hari terpanas di Jakarta
suhu_jakarta = suhu[0]  # atau suhu[kota == "Jakarta"][0]
hari_terpanas = suhu_jakarta.argmax()
print(f"Jakarta terpanas di hari ke-{hari_terpanas}")  # index 5 (hari ke-6)

# 3. Kota dengan rata-rata di bawah 25
rata_per_kota = suhu.mean(axis=1)
mask_dingin = rata_per_kota < 25
print("Kota rata-rata < 25°C:", kota[mask_dingin])  # ['Bandung' 'Malang']

# 4. Clip suhu Malang minimal 17
suhu_malang = suhu[3]
suhu_malang_clipped = np.clip(suhu_malang, 17, None)  # None = tanpa batas atas
print("Suhu Malang setelah clip:", suhu_malang_clipped)  # [18 17 19 17 18 20 17]
```
</details>

---

## ✅ Checklist Kelulusan Milestone 2

- [ ] Bisa indexing & slicing array 1D dan 2D (`arr[start:stop:step]`, `arr[baris, kolom]`)
- [ ] Paham beda **view** (dari slicing) vs **copy** (dari `.copy()` atau fancy indexing) — ini paling sering jadi sumber bug!
- [ ] Bisa pakai `np.where()` buat conditional replace dan cari index
- [ ] Bisa pakai `np.clip()` buat membatasi rentang nilai
- [ ] Paham fancy indexing (`arr[[i, j, k]]`) dan boolean masking (`arr[arr > x]`)
- [ ] Bisa kombinasikan boolean mask di satu array untuk filter array lain yang "sejajar" (soal 17, 25)

Kalau ada soal yang bikin nyangkut, bilang aja nomornya. Lanjut ke **Milestone 3: Broadcasting, Reshaping, & Array Manipulation** kalau udah pede?
