import random


def get_matrix():
    arr = []

    for i in range(matrix_size[0]):
        arr.append([])
        for j in range(matrix_size[1]):
            arr[i].append(random.randint(-100, 100))

    return arr


matrix_size = list(map(int, input('Введите размер матрицы через пробел: ').split()))

matrix_1 = get_matrix()
matrix_2 = get_matrix()
matrix_3 = []

for i in range(len(matrix_1)):
    matrix_3.append([])

    for j in range(len(matrix_1[i])):
        matrix_3[i].append(matrix_1[i][j] + matrix_2[i][j])

print(matrix_3)
