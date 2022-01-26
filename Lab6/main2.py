"""Lab6.2 Python 3.10.2"""
import sys
import math
from random import randint

N = 6
matrix = [[randint(-11, 11) for i in range(N)] for j in range(N)]

print("Сгенерированная матрица:")
for row in matrix:
    for elem in row:
        print(f"{elem:>5}", end=" ")
    print()

# Получение индексов столбцов не содержащих числа > 10 по модулю.
column_indexes = []
for column in range(N):
    flag = True
    for row in range(N):
        if math.fabs(matrix[row][column]) > 10:
            flag = False
            break
    if flag:
        column_indexes.append(column)

if not column_indexes:
    print("Нет подходящих столбцов.")
    sys.exit(1)

column_prods = []
for column in column_indexes:
    column_prod = 1
    for row in range(N):
        column_prod *= matrix[row][column]
    column_prods.append(column_prod)

min_column = column_indexes[column_prods.index(min(column_prods))]
print(f"Столбец с наименьшим произведением элементов: {min_column}")

nearby_column = min_column + 1 if min_column + 1 < N else min_column - 1
for row in matrix:
    tmp = row[nearby_column]
    row[nearby_column] = row[min_column]
    row[min_column] = tmp

print("Матрица после перестановки:")
for row in matrix:
    for elem in row:
        print(f"{elem:>5}", end=" ")
    print()
