"""Lab7.1 Python 3.10.2"""
import sys

def is_prime(d):
    """Проверка простоты."""
    if d == 2 or d == 3: return True
    if d % 2 == 0 or d < 2: return False

    for div in range(3, int(d ** 0.5) + 1, 2):
        if d % div == 0:
            return False
    return True

try:
    n = int(input("n > 2: "))
    if n <= 2: raise ValueError
except ValueError:
    print("Ошибка: Некорректный ввод.")
    sys.exit(2)

nums = [i for i in range(n, n * 2 + 1)]
print(f"Диапазон: {nums}")
prime_nums = [i for i in nums if is_prime(i)]

print("Пары чисел близнецов:")
for i in range(0, len(prime_nums) - 1):
    if prime_nums[i + 1] == prime_nums[i] + 2:
        print(f"{prime_nums[i]}, {prime_nums[i + 1]}")
