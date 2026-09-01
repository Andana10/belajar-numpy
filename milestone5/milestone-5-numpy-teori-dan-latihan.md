# 📘 Milestone 5: Matematika, Statistik, & Linear Algebra

> Ini milestone PALING KRUSIAL buat jalur ML/AI Engineer. Kenapa? Karena training model ML itu **secara harfiah** adalah operasi matriks berulang-ulang. Kita bahas teori tiap bagian, latihan, dan di akhir ada studi kasus yang literally ngebangun algoritma ML dari nol pakai NumPy murni.

---

## 📖 TEORI BAGIAN A: Fungsi Matematika Universal (ufuncs)

### Apa itu ufunc?
Universal functions (ufuncs) adalah fungsi matematika yang otomatis bekerja **elementwise** ke seluruh array — tanpa loop, dan biasanya sangat cepat karena diimplementasi di level C.

```python
import numpy as np
arr = np.array([1, 4, 9, 16, 25])
print(np.sqrt(arr))    # [1. 2. 3. 4. 5.]
print(np.exp(arr))     # e^x untuk tiap elemen
print(np.log(arr))     # ln(x) untuk tiap elemen
```

### Kenapa Penting untuk ML?
Hampir semua fungsi aktivasi di neural network (sigmoid, ReLU, softmax) itu dibangun dari ufuncs ini:
```python
def sigmoid(x):
    return 1 / (1 + np.exp(-x))   # ini persis fungsi aktivasi di neural network!
```

---

## 🟢 LATIHAN BAGIAN A: Ufuncs

### Soal 1
Diberikan `x = np.array([-2, -1, 0, 1, 2])`. Implementasikan fungsi **sigmoid**: `1 / (1 + e^(-x))`, hitung untuk semua elemen sekaligus.

<details>
<summary>🔑 Jawaban</summary>

```python
x = np.array([-2, -1, 0, 1, 2])
sigmoid = 1 / (1 + np.exp(-x))
print(sigmoid)  # [0.119 0.269 0.5   0.731 0.881] (dibulatkan)
```
**Insight:** Perhatikan hasilnya selalu antara 0-1 — makanya sigmoid dipakai buat probabilitas di klasifikasi biner.
</details>

---

### Soal 2
Implementasikan fungsi **ReLU** (Rectified Linear Unit): `max(0, x)` — fungsi aktivasi paling umum di deep learning. Gunakan `np.maximum()` (BUKAN `.max()` — beda fungsi!).

<details>
<summary>🔑 Jawaban</summary>

```python
x = np.array([-3, -1, 0, 2, 5])
relu = np.maximum(0, x)
print(relu)  # [0 0 0 2 5]
```
**Beda `np.maximum()` vs `.max()`:** `.max()` cari SATU nilai terbesar dari array, `np.maximum(a, b)` bandingin elementwise antara dua nilai/array dan ambil yang lebih besar di tiap posisi.
</details>

---

### Soal 3
Diberikan skor mentah (logits) dari model klasifikasi 3 kelas: `logits = np.array([2.0, 1.0, 0.1])`. Implementasikan **softmax**: `exp(x_i) / sum(exp(x))` — ini yang mengubah skor mentah jadi probabilitas.

<details>
<summary>🔑 Jawaban</summary>

```python
logits = np.array([2.0, 1.0, 0.1])
exp_logits = np.exp(logits)
softmax = exp_logits / exp_logits.sum()
print(softmax)          # [0.659 0.242 0.099] (dibulatkan)
print(softmax.sum())    # 1.0 -> selalu total 100%, ini ciri khas softmax
```
</details>

---

### Soal 4
Diberikan prediksi model `y_pred = np.array([0.9, 0.1, 0.8, 0.3])` dan label asli `y_true = np.array([1, 0, 1, 0])`. Hitung **Mean Squared Error (MSE)**: rata-rata dari `(y_pred - y_true)^2`.

<details>
<summary>🔑 Jawaban</summary>

```python
y_pred = np.array([0.9, 0.1, 0.8, 0.3])
y_true = np.array([1, 0, 1, 0])
mse = np.mean((y_pred - y_true) ** 2)
print(mse)  # 0.0225
```
**Ini fungsi loss paling dasar** yang bakal terus kamu temuin di ML — dan lihat, cuma butuh 1 baris NumPy!
</details>

---

## 📖 TEORI BAGIAN B: Statistik Deskriptif Lanjutan

### Lebih dari Sekadar Mean & Std
Kamu udah kenal `.mean()`, `.std()`, `.sum()` dari milestone sebelumnya. Sekarang kita tambah beberapa yang penting untuk ML:

```python
data = np.array([23, 45, 12, 67, 34, 89, 21])

print(np.median(data))       # nilai tengah -> lebih tahan outlier daripada mean
print(np.percentile(data, 25))  # kuartil 1 (Q1)
print(np.percentile(data, 75))  # kuartil 3 (Q3)
print(np.var(data))          # variance (std kuadrat)
```

### Korelasi & Kovarians
Ini KRUSIAL untuk feature selection di ML — mencari hubungan antar variabel:
```python
jam_belajar = np.array([1, 2, 3, 4, 5])
nilai_ujian = np.array([50, 55, 65, 70, 85])

korelasi_matrix = np.corrcoef(jam_belajar, nilai_ujian)
print(korelasi_matrix)
# [[1.        0.98      ]
#  [0.98      1.        ]]
```
`np.corrcoef()` mengembalikan matriks korelasi. Nilai `0.98` (di luar diagonal) berarti hubungan yang SANGAT kuat antara jam belajar dan nilai ujian — mendekati `1` = korelasi positif sempurna.

---

## 🟡 LATIHAN BAGIAN B: Statistik Lanjutan

### Soal 5
Diberikan data gaji karyawan yang ada outlier ekstrem: `gaji = np.array([5000000, 5500000, 4800000, 6000000, 500000000])` (nilai terakhir kemungkinan salah input). Bandingkan `.mean()` vs `np.median()` — kenapa hasilnya beda jauh?

<details>
<summary>🔑 Jawaban</summary>

```python
gaji = np.array([5000000, 5500000, 4800000, 6000000, 500000000])
print("Mean:", gaji.mean())      # 104260000 -> sangat terpengaruh outlier!
print("Median:", np.median(gaji)) # 5500000 -> jauh lebih representatif
```
**Insight penting untuk ML:** Outlier bisa "menyesatkan" statistik ringkasan. Ini kenapa di preprocessing data ML, kamu sering perlu cek median vs mean untuk deteksi outlier sebelum training model.
</details>

---

### Soal 6
Diberikan dua fitur dari dataset: `luas_rumah = np.array([50, 70, 90, 120, 150])` (m²) dan `harga_rumah = np.array([300, 420, 550, 700, 900])` (juta). Hitung korelasi antara keduanya pakai `np.corrcoef()`, dan interpretasikan hasilnya.

<details>
<summary>🔑 Jawaban</summary>

```python
luas_rumah = np.array([50, 70, 90, 120, 150])
harga_rumah = np.array([300, 420, 550, 700, 900])

korelasi = np.corrcoef(luas_rumah, harga_rumah)
print(korelasi[0, 1])  # ambil nilai korelasi (bukan diagonal) -> sekitar 0.998
```
**Interpretasi:** Korelasi ~0.998 artinya luas rumah dan harga rumah punya hubungan linear yang SANGAT kuat — fitur `luas_rumah` ini kemungkinan besar akan jadi prediktor yang bagus untuk model prediksi harga.
</details>

---

### Soal 7
Diberikan nilai ujian `nilai = np.array([45, 60, 65, 70, 72, 75, 78, 80, 85, 95])`. Deteksi outlier menggunakan aturan **IQR (Interquartile Range)**: outlier adalah nilai di bawah `Q1 - 1.5*IQR` atau di atas `Q3 + 1.5*IQR`, dimana `IQR = Q3 - Q1`.

<details>
<summary>🔑 Jawaban</summary>

```python
nilai = np.array([45, 60, 65, 70, 72, 75, 78, 80, 85, 95])

Q1 = np.percentile(nilai, 25)
Q3 = np.percentile(nilai, 75)
IQR = Q3 - Q1

batas_bawah = Q1 - 1.5 * IQR
batas_atas = Q3 + 1.5 * IQR

mask_outlier = (nilai < batas_bawah) | (nilai > batas_atas)
print("Outlier:", nilai[mask_outlier])
```
**Ini teknik deteksi outlier standar** yang sering dipakai di tahap EDA sebelum training model ML.
</details>

---

## 📖 TEORI BAGIAN C: Linear Algebra Dasar — Dot Product & Matrix Multiplication

### Dot Product (Perkalian Titik)
Dot product antara dua vektor adalah jumlah dari perkalian elemen-elemen yang sejajar — hasilnya SATU angka (scalar):
```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
hasil = np.dot(a, b)   # 1*4 + 2*5 + 3*6 = 32
print(hasil)  # 32
```

### Kenapa Dot Product Penting Banget di ML?
Ini adalah **operasi inti** dari hampir semua model ML linear:
```python
# Prediksi linear regression: y = w1*x1 + w2*x2 + ... + bias
fitur = np.array([2, 3, 1])       # nilai fitur (x)
bobot = np.array([0.5, 0.3, 0.2]) # bobot yang dipelajari model (w)
prediksi = np.dot(fitur, bobot)   # ini PERSIS cara neural network menghitung 1 neuron!
```

### Matrix Multiplication dengan `@`
Untuk perkalian matriks (bukan cuma vektor), gunakan operator `@` atau `np.matmul()`:
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
hasil = A @ B
print(hasil)
# [[19 22]
#  [43 50]]
```
**PENTING — Beda dengan perkalian elementwise (`*`):**
```python
A * B   # elementwise: [[1*5, 2*6], [3*7, 4*8]] = [[5,12],[21,32]]
A @ B   # matrix mult:  aturan baris-kali-kolom -> [[19,22],[43,50]]
```
Ini salah satu **kesalahan paling umum** pemula ML: pakai `*` padahal maksudnya `@`, atau sebaliknya. Selalu cek dulu operasi mana yang kamu maksud!

---

## 🟠 LATIHAN BAGIAN C: Dot Product & Matrix Multiplication

### Soal 8
Diberikan vektor fitur rumah `fitur = np.array([100, 3, 10])` (luas m², jumlah kamar, umur bangunan tahun) dan bobot model `bobot = np.array([2.5, 50, -1.2])`. Hitung prediksi harga pakai dot product, lalu tambahkan bias `10`.

<details>
<summary>🔑 Jawaban</summary>

```python
fitur = np.array([100, 3, 10])
bobot = np.array([2.5, 50, -1.2])
bias = 10

prediksi = np.dot(fitur, bobot) + bias
print(prediksi)  # 100*2.5 + 3*50 + 10*-1.2 + 10 = 250+150-12+10 = 398
```
**Ini PERSIS formula linear regression:** `y = w·x + b`.
</details>

---

### Soal 9
Diberikan dua matriks `A = np.array([[2,0],[1,3]])` dan `B = np.array([[1,2],[3,4]])`. Hitung `A @ B` dan `B @ A` — buktikan bahwa perkalian matriks **TIDAK komutatif** (urutan penting!).

<details>
<summary>🔑 Jawaban</summary>

```python
A = np.array([[2,0],[1,3]])
B = np.array([[1,2],[3,4]])

print(A @ B)
# [[ 2  4]
#  [10 14]]

print(B @ A)
# [[ 4  6]
#  [10 12]]
```
**Insight:** Hasilnya BEDA! Beda dengan perkalian angka biasa (`2*3 == 3*2`), perkalian matriks urutannya menentukan hasil. Ini penting dipahami karena di neural network, urutan perkalian matriks antar layer itu krusial.
</details>

---

### Soal 10
Studi kasus: Kamu punya data 3 rumah dengan 2 fitur (luas, kamar):
```python
X = np.array([
    [100, 3],
    [150, 4],
    [80, 2]
])
```
dan bobot model `w = np.array([2.0, 30])` plus bias `5`. Hitung prediksi untuk **SEMUA rumah sekaligus** dalam satu operasi matrix multiplication (`X @ w + bias`) — tanpa loop.

<details>
<summary>🔑 Jawaban</summary>

```python
X = np.array([
    [100, 3],
    [150, 4],
    [80, 2]
])
w = np.array([2.0, 30])
bias = 5

prediksi = X @ w + bias
print(prediksi)  # [295. 425. 170.]
```
**Ini persis cara kerja batch prediction di ML** — satu operasi matrix multiplication menghasilkan prediksi untuk BANYAK data sekaligus, jauh lebih efisien daripada loop satu-satu.
</details>

---

## 📖 TEORI BAGIAN D: Linear Algebra Lanjutan (`np.linalg`)

### Transpose (Recap dari M3) + Determinant & Inverse
```python
A = np.array([[4, 2], [7, 6]])

print(np.linalg.det(A))   # determinant: 4*6 - 2*7 = 10
print(np.linalg.inv(A))   # invers matriks (kayak "1/A" versi matriks)
```
**Kegunaan inverse:** Menyelesaikan sistem persamaan linear, dan jadi dasar dari **Normal Equation** untuk linear regression (lihat studi kasus di bawah).

### Menyelesaikan Sistem Persamaan Linear
```python
# Sistem: 2x + y = 5 ; x + 3y = 10
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 10])
x = np.linalg.solve(A, b)
print(x)  # [1. 3.] -> x=1, y=3
```

### Eigenvalues & Eigenvectors
Konsep ini dasar dari **PCA (Principal Component Analysis)** — teknik reduksi dimensi yang sangat umum di ML:
```python
A = np.array([[2, 0], [0, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
```

---

## 🔴 LATIHAN BAGIAN D: np.linalg

### Soal 11
Hitung determinant dari `A = np.array([[3, 1], [2, 4]])`. Jika determinant = 0, matriks tersebut disebut **singular** (tidak punya inverse) — kenapa ini penting diketahui sebelum coba invers suatu matriks?

<details>
<summary>🔑 Jawaban</summary>

```python
A = np.array([[3, 1], [2, 4]])
det = np.linalg.det(A)
print(det)  # 10.0
```
**Kenapa penting:** Kalau determinant = 0, `np.linalg.inv()` akan error atau menghasilkan angka yang tidak stabil (inf/nan). Di ML, ini relevan misalnya saat fitur-fitur di data kamu punya multikolinearitas sempurna (satu fitur adalah kombinasi linear dari fitur lain) — bisa bikin model linear regression gagal dihitung.
</details>

---

### Soal 12
Selesaikan sistem persamaan linear berikut pakai `np.linalg.solve()`:
```
3x + 2y = 12
x - y = 1
```

<details>
<summary>🔑 Jawaban</summary>

```python
A = np.array([[3, 2], [1, -1]])
b = np.array([12, 1])
hasil = np.linalg.solve(A, b)
print(hasil)  # [2.8 2.2] (x=2.8, y=2.2)
```
</details>

---

### Soal 13
Diberikan matriks `A = np.array([[4, 2], [1, 3]])`. Hitung inverse-nya pakai `np.linalg.inv()`, lalu buktikan bahwa `A @ A_inverse` menghasilkan **matriks identitas** (aturan matematis: `A x A^-1 = I`).

<details>
<summary>🔑 Jawaban</summary>

```python
A = np.array([[4, 2], [1, 3]])
A_inv = np.linalg.inv(A)
print(A_inv)

hasil = A @ A_inv
print(np.round(hasil, decimals=10))  # [[1. 0.] [0. 1.]] -> matriks identitas
```
**Catatan:** Kita bulatkan pakai `np.round()` karena floating point kadang menghasilkan angka super kecil kayak `1e-17` yang seharusnya `0` (ini fenomena umum di komputasi numerik).
</details>

---

## 🏆 BAGIAN E — STUDI KASUS BESAR: Bangun Linear Regression dari Nol

> Ini capstone project Milestone 5 — kamu akan implementasi algoritma ML asli (linear regression) HANYA pakai NumPy, tanpa Scikit-learn. Tujuannya supaya kamu paham betul apa yang terjadi "di balik layar" saat nanti kamu pakai `model.fit()` di library ML.

### Konsep: Normal Equation
Linear regression punya solusi analitik (rumus langsung, tanpa iterasi) yang disebut **Normal Equation**:

$$w = (X^T X)^{-1} X^T y$$

Dimana:
- $X$ = matriks fitur (ditambah kolom bias/intercept)
- $y$ = vektor target
- $w$ = vektor bobot yang mau dicari (termasuk bias)

### Soal 14
Diberikan data sederhana hubungan jam belajar (X) dan nilai ujian (y):
```python
jam_belajar = np.array([1, 2, 3, 4, 5])
nilai_ujian = np.array([52, 58, 65, 73, 80])
```
Langkah-langkah:
1. Tambahkan kolom bias (isi `1`) ke `X` supaya modelnya punya intercept
2. Terapkan rumus Normal Equation untuk mencari bobot `w` (termasuk bias)
3. Gunakan `w` untuk memprediksi nilai ujian kalau belajar **6 jam**

<details>
<summary>🔑 Jawaban</summary>

```python
jam_belajar = np.array([1, 2, 3, 4, 5])
nilai_ujian = np.array([52, 58, 65, 73, 80])

# 1. Tambah kolom bias (kolom pertama isi 1 semua)
X = np.column_stack([np.ones(len(jam_belajar)), jam_belajar])
print(X)
# [[1. 1.]
#  [1. 2.]
#  [1. 3.]
#  [1. 4.]
#  [1. 5.]]

y = nilai_ujian

# 2. Normal Equation: w = (X^T X)^-1 X^T y
w = np.linalg.inv(X.T @ X) @ X.T @ y
print("Bobot (bias, slope):", w)
# sekitar [44.4, 7.1] -> bias≈44.4, slope≈7.1

# 3. Prediksi untuk 6 jam belajar
jam_baru = np.array([1, 6])   # [bias, jam]
prediksi = jam_baru @ w
print("Prediksi nilai untuk 6 jam belajar:", prediksi)  # sekitar 87
```
**INI ADALAH INTI dari bagaimana Scikit-learn's `LinearRegression().fit()` bekerja di baliknya!** Kamu baru saja membangun algoritma ML pertamamu murni pakai konsep Milestone 1-5: array, indexing, broadcasting, dan linear algebra. Setelah ini, saat kamu pakai Scikit-learn, kamu akan paham APA yang terjadi, bukan cuma "cara pakainya".
</details>

---

### Soal 15 (Bonus Ekstra — Gradient Descent Sederhana)
Sebagai alternatif dari Normal Equation, ML modern lebih sering pakai **Gradient Descent** (iteratif, cocok untuk data besar). Implementasikan versi sederhana untuk mencari `slope` dan `bias` dari data yang sama di Soal 14, dengan update rule:
```
bias_baru = bias - learning_rate * gradien_bias
slope_baru = slope - learning_rate * gradien_slope
```
dimana gradien dihitung dari turunan MSE.

<details>
<summary>🔑 Jawaban</summary>

```python
jam_belajar = np.array([1, 2, 3, 4, 5], dtype=float)
nilai_ujian = np.array([52, 58, 65, 73, 80], dtype=float)

# Inisialisasi
bias = 0.0
slope = 0.0
learning_rate = 0.01
n = len(jam_belajar)

for iterasi in range(1000):
    prediksi = slope * jam_belajar + bias
    error = prediksi - nilai_ujian

    gradien_slope = (2/n) * np.dot(error, jam_belajar)
    gradien_bias = (2/n) * error.sum()

    slope -= learning_rate * gradien_slope
    bias -= learning_rate * gradien_bias

print(f"Slope: {slope:.2f}, Bias: {bias:.2f}")
# Harusnya mendekati hasil Normal Equation: slope≈7.1, bias≈44.4
```
**Insight:** Perhatikan SEMUA operasi di dalam loop (perkalian, dot product, sum) adalah vectorized — nggak ada loop manual per elemen data. Ini pola yang PERSIS dipakai di training neural network sungguhan, cuma skalanya jauh lebih besar (jutaan parameter, bukan cuma 2).
</details>

---

## ✅ Checklist Kelulusan Milestone 5

- [ ] Paham ufuncs dan bisa implementasi fungsi aktivasi ML (sigmoid, ReLU, softmax) dari NumPy murni
- [ ] Bisa hitung statistik lanjutan: median, percentile, IQR untuk deteksi outlier
- [ ] Paham korelasi (`np.corrcoef()`) dan kegunaannya untuk feature selection
- [ ] **Paham beda `*` (elementwise) vs `@` (matrix multiplication)** — ini WAJIB banget buat ML
- [ ] Bisa pakai `np.linalg.inv()`, `np.linalg.det()`, `np.linalg.solve()`
- [ ] Berhasil implementasi Linear Regression dari nol pakai Normal Equation
- [ ] (Bonus) Berhasil implementasi Gradient Descent sederhana

Kalau checklist ini semua tercentang, kamu sudah punya **fondasi matematis riil** untuk mulai Scikit-learn, dan bahkan sudah "mencicipi" cara kerja neural network training. Ini modal yang jauh lebih kuat dibanding orang yang langsung loncat ke `model.fit()` tanpa paham isinya.
