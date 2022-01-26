"""Lab3 Python 3.10.2"""
import sys

try:
    num1 = float(input("Первое число: "))
    num2 = float(input("Второе число: "))
    num3 = float(input("Третье число: "))
except ValueError:
    print("Ошибка: Некорректный ввод.")
    sys.exit(2)

positive_nums_n = 0
if num1 > 0: positive_nums_n += 1
if num2 > 0: positive_nums_n += 1
if num3 > 0: positive_nums_n += 1

print(f"Введено {positive_nums_n} положительных чисел")
