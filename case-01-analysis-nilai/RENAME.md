# Case 01 — Analisis Nilai Mahasiswa 

##  Tujuan
Melatih penggunaan List Comprehension, Lambda Function, Filtering, dan Sorting dalam studi kasus nyata perhitungan nilai akademik mahasiswa.

##  Konsep Python yang Dipakai
- List Comprehension → menghitung nilai akhir secara efisien
- `filter()` + `lambda` → menyaring mahasiswa berprestasi
- `sorted()` + `key=lambda` → membuat ranking kelas secara descending
- `enumerate()` → memberi nomor peringkat otomatis
- Formatted String (`f-string`) → menampilkan output rapi dengan alignment
- String Multiplication (`"-"  50`) → membuat separator visual

##  Rumus Nilai Akhir

| Komponen | Bobot |
|----------|-------|
| Tugas    | 30%   |
| UTS      | 30%   |
| UAS      | 40%   |

## 🔍 Fitur Program

Program menampilkan **4 bagian utama**:

### [1] Daftar Seluruh Mahasiswa
Menampilkan semua mahasiswa beserta nilai akhir yang sudah dihitung.

### [2] Mahasiswa Berprestasi
Filter mahasiswa dengan **nilai akhir > 80**. Jika tidak ada, tampilkan pesan "Tidak ada mahasiswa dengan nilai di atas 80."

### [3] Peringkat Kelas (Ranking)
Urutkan seluruh mahasiswa dari nilai tertinggi ke terendah menggunakan `sorted()` + `lambda`.

### [4] Mahasiswa Terbaik
Ambil elemen pertama dari ranking (`ranking[0]`) sebagai mahasiswa terbaik.

## 📋 Struktur Data

```python
data_mahasiswa = [
    {"nama": "Aisyah",   "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi",     "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika",  "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dewi",     "nim": "230104", "tugas": 95, "uts": 90, "uas": 85},
    {"nama": "Eko",      "nim": "230105", "tugas": 60, "uts": 70, "uas": 65},
]