# ============================================
# STUDI KASUS 1 - Analisis Nilai Mahasiswa
# ============================================

# Data awal mahasiswa
data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dewi", "nim": "230104", "tugas": 95, "uts": 90, "uas": 85},
    {"nama": "Eko", "nim": "230105", "tugas": 60, "uts": 70, "uas": 65},
]

# 1. Hitung Nilai Akhir (Tugas 30%, UTS 30%, UAS 40%)
for mhs in data_mahasiswa:
    mhs["nilai_akhir"] = round(
        (mhs["tugas"] * 0.30) + (mhs["uts"] * 0.30) + (mhs["uas"] * 0.40), 2
    )

# 2. Filter Mahasiswa Berprestasi (nilai akhir > 80)
mahasiswa_berprestasi = list(
    filter(lambda m: m["nilai_akhir"] > 80, data_mahasiswa)
)

# 3. Ranking dari nilai tertinggi ke terendah
ranking = sorted(data_mahasiswa, key=lambda m: m["nilai_akhir"], reverse=True)

# 4. Tampilkan Output
print("=" * 50)
print("       HASIL ANALISIS NILAI MAHASISWA")
print("=" * 50)

print("\n[1] DAFTAR NILAI AKHIR SEMUA MAHASISWA")
print("-" * 50)
for m in data_mahasiswa:
    print(f"  {m['nama']:10} ({m['nim']}) -> Nilai Akhir: {m['nilai_akhir']}")

print("\n[2] MAHASISWA BERPRESTASI (Nilai > 80)")
print("-" * 50)
if mahasiswa_berprestasi:
    for m in mahasiswa_berprestasi:
        print(f"  {m['nama']:10} ({m['nim']}) -> Nilai Akhir: {m['nilai_akhir']}")
else:
    print("  Tidak ada mahasiswa dengan nilai di atas 80.")

print("\n[3] PERINGKAT KELAS (Ranking)")
print("-" * 50)
for i, m in enumerate(ranking, 1):
    print(f"  Rank {i}: {m['nama']:10} -> {m['nilai_akhir']}")

print("\n[4] MAHASISWA TERBAIK")
print("-" * 50)
terbaik = ranking[0]
print(f"  Nama       : {terbaik['nama']}")
print(f"  NIM        : {terbaik['nim']}")
print(f"  Nilai Akhir: {terbaik['nilai_akhir']}")
print("=" * 50)