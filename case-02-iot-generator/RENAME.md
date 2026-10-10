---

##  3. `case-02-iot-generator/README.md`

```markdown
# Case 02 — Streaming Data Sensor IoT 🌡️

##  Tujuan
Melatih penggunaan **Generator Function**, **`yield`**, dan **Iterator Pattern** untuk simulasi streaming data sensor yang hemat memori.

##  Konsep Python yang Dipakai
- Generator Function (`yield`) → mengeluarkan data satu per satu tanpa menyimpan seluruh data di memori
- `next()` → mengambil nilai berikutnya dari generator
- Kategorisasi kondisional → mengelompokkan suhu ke kategori Dingin / Normal / Panas
- `time.sleep()` → mensimulasikan delay pembacaan sensor real-time

##  Kategori (Suhu)
| Rentang Suhu | Kategori |
|--------------|----------|
| < 20°C       | Dingin   |
| 20°C – 30°C  | Normal   |
| > 30°C       | Panas    |

##  Cara Menjalankan

```bash
cd case-02-iot-generator
python main.py