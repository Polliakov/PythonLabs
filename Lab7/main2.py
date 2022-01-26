"""Lab7.2 Python 3.10.2"""
from random import randint

N1 = 5
N2 = 7

def print_matrix(matrix, title="Matrix:"):
    """Print int matrix."""
    print(title)
    for row in matrix:
        for elem in row:
            print(f"{elem:>5}", end=" ")
        print()

def matrix_max(matrix):
    """Return tuple with indexes (i, j) of max element in matrix."""
    max_elem = matrix[0][0]
    max_index = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_elem:
                max_elem = matrix[i][j]
                max_index = i, j
    return max_index

a = [[randint(0, 100) for j in range(N1)] for i in range(N2)]
b = [[randint(0, 100) for j in range(N2)] for i in range(N1)]

print("Сгенерированные матрицы:")
print_matrix(a, "Матрица А:")
print_matrix(b, "Матрица В:")

a_max = matrix_max(a)
b_max = matrix_max(b)

print(f"Индексы максимальных элементов: A{a_max} B{b_max}\n")

tmp = b[b_max[0]][b_max[1]]
b[b_max[0]][b_max[1]] = a[a_max[0]][a_max[1]]
a[a_max[0]][a_max[1]] = tmp

print("Матрицы после перестановки:")
print_matrix(a, "Матрица А:")
print_matrix(b, "Матрица В:")
