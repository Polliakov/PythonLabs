"""Lab4.2 Python 3.10.2"""
import sys

try:
    n = int(input("Целое число > 0: "))
    if n <= 0: raise ValueError
except ValueError:
    print("Ошибка: Некорректный ввод.")
    sys.exit(2)

k = 0
while (k + 1)**2 <= n:
    k += 1

print(f"K^2 <= {n}: {k}")
