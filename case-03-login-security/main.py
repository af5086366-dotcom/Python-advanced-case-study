import re
from datetime import datetime

# ============================================
# 1. DECORATOR: Audit Log + Lockout
# ============================================
def audit_log(func):
    def wrapper(self, username, password):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Cek lockout
        if self._failed_attempts >= 3:
            print(f"[{waktu}] User: {username} | Status: LOCKED | Akun terkunci.")
            return False, "Akun terkunci"

        hasil, alasan = func(self, username, password)

        if not hasil:
            self._failed_attempts += 1
        else:
            self._failed_attempts = 0

        status = "BERHASIL" if hasil else "DITOLAK"
        print(f"[{waktu}] User: {username} | Status: {status} | Alasan: {alasan}")
        return hasil
    return wrapper


# ============================================
# 2. CLASS USER: Enkapsulasi dengan @property
# ============================================
class User:
    def __init__(self, username, password):
        self._username = None
        self._password = None
        self._failed_attempts = 0
        self.username = username   # trigger setter
        self.password = password   # trigger setter

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.match(r"^[a-zA-Z0-9]{5,}$", value):
            raise ValueError("Username tidak valid! Minimal 5 karakter alfanumerik.")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not re.match(r"^(?=.*\d).{8,}$", value):
            raise ValueError("Password tidak valid! Minimal 8 karakter dan mengandung angka.")
        self._password = value

    @audit_log
    def login(self, username, password):
        if username == self._username and password == self._password:
            return True, "Login sukses"
        return False, "Username atau password salah"


# ============================================
# 3. MAIN: Skenario Pengujian
# ============================================
if __name__ == "__main__":
    print("=== SKENARIO PENGUJIAN LOGIN ===\n")

    # Skenario 1: Username terlalu pendek
    try:
        user1 = User("adm", "password123")
    except ValueError as e:
        print(f"Error saat buat user: {e}\n")

    # Skenario 2: Password tanpa angka
    try:
        user2 = User("admin123", "passwordku")
    except ValueError as e:
        print(f"Error saat buat user: {e}\n")

    # Skenario 3: Sukses buat user + uji login
    try:
        user3 = User("budisantoso", "rahasia123")
        print("User berhasil dibuat.\n")

        # Login gagal (password salah)
        user3.login("budisantoso", "salah123")

        # Login gagal 2x lagi -> test lockout
        user3.login("budisantoso", "salah456")
        user3.login("budisantoso", "salah789")

        # Login ke-4 -> harus LOCKED
        user3.login("budisantoso", "rahasia123")

    except ValueError as e:
        print(f"Error: {e}")