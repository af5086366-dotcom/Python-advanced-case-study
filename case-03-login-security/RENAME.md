# Case 03 — Sistem Keamanan Akun & Audit Log 

##  Tujuan
Melatih penggunaan RegEx, Decorator/Closure, dan `@property` untuk membangun sistem validasi akun dengan pencatatan log otomatis serta fitur **lockout** setelah 3x gagal login.

##  Konsep Python yang Dipakai
- RegEx (`re`)→ validasi format username & password
- **Decorator (`@audit_log`) → mencatat setiap percobaan login tanpa mengubah fungsi utama
- **Closure → decorator menyimpan referensi ke fungsi asli
- `@property` + setter → enkapsulasi validasi otomatis saat assignment
- datetime` → timestamp log
- State tracking (`self._failed_attempts`) → menghitung percobaan login gagal untuk fitur lockout

##  Aturan Validasi

### Username
- Minimal 5 karakter
- Hanya alfanumerik (huruf & angka)
- Tanpa spasi atau simbol

Regex: `^[a-zA-Z0-9]{5,}$`

### Password
- Minimal 8 karakter
- Harus mengandung minimal 1 angka

Regex: `^(?=.*\d).{8,}$`

##  Fitur Keamanan

| Fitur | Deskripsi |
|-------|-----------|
| Validasi Real-time | Setter `@property` langsung menolak input tidak valid |
| Audit Log| Setiap percobaan login dicatat dengan timestamp |
| **Lockout Otomatis | Akun terkunci setelah 3x gagal login|
| Reset Counter | Counter gagal direset ke 0 setiap login berhasil |

## Format Audit Log