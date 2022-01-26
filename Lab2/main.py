"""Lab2 Python 3.10.2"""
import math
import sys

try:
    y = float(input("y = "))
    n = float(input("n = "))
except ValueError:
    print("Ошибка: Некорректный ввод.")
    sys.exit(2)

d = y**2 + (0.5 * n + 4.8) / math.sin(y)

print(f"d = {d:.2f}")
