"""Lab6.1 Python 3.10.2"""
import sys
from random import uniform

try:
    n = int(input("Порядок матрицы: "))
    if n < 0: raise ValueError
except ValueError:
    print("Ошибка: Некорректный ввод.")
    sys.exit(2)

matrix = [[uniform(-10, 10) for i in range(n)] for j in range(n)]

print("Сгенерированная матрица:")
for row in matrix:
    for elem in row:
        print(f"{elem:>6.2f}", end=" ")
    print()

min_rows = [min(row) for row in matrix]
min_elem_row_index = min_rows.index(min(min_rows))
row_sum = sum(matrix[min_elem_row_index])

print(f"Сумма ряда с минимальным элементом: {row_sum:.2f}")
