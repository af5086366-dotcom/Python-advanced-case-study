import random, time
from collections import Counter

def sensor_suhu_generator(min_val=15.0, max_val=38.0):
    while True:
        yield round(random.uniform(min_val, max_val), 1)

def kategorikan(suhu: float) -> str:
    return "Dingin" if suhu < 20 else "Normal" if suhu <= 30 else "Panas"

# Bonus: statistik distribusi
sensor = sensor_suhu_generator()
statistik = Counter()
for i in range(1, 11):
    suhu = next(sensor)
    kat = kategorikan(suhu)
    statistik[kat] += 1
    print(f"Pembacaan {i:02d}: {suhu}°C -> {kat}")
    time.sleep(0.5)

print("\n=== DISTRIBUSI ===")
for kat, jml in statistik.items():
    print(f"{kat}: {jml}x")