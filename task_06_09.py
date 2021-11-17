"""Task_06_09
Обнулить все элементы матрицы выше главной диагонали."""

from random import randint

n = 4
m = 4
arr = []

for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(1, 9)
        arr1.append(p)
    arr.append(arr1)

i = 0
while i < n:
    j = i + 1
    while j < n:
        arr[i][j] = 0
        j += 1
    i += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()  # Печатаем для проверки

"""Task_06_10
Обнулить все элементы матрицы ниже главной диагонали"""

i = 1
while i < n:
    j = 0
    while j < i:
        arr[i][j] = 0
        j += 1
    i += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()

"""Task_06_11
Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m"""

from random import randint

n = 4
m = 5
matrix_a = []
matrix_b = []

for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(1, 9)
        arr1.append(p)
    matrix_a.append(arr1)

for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(1, 9)
        arr1.append(p)
    matrix_b.append(arr1)

print(matrix_a)
print(matrix_b)

""" Task_06_12
Создать матрицу равную сумме matrix_a и matrix_b."""

matrix_c = []
for i in range(n):
    c_list = []
    for j in range(m):
        elem = matrix_a[i][j] + matrix_b[i][j]
        c_list.append(elem)
    matrix_c.append(c_list)
print(matrix_c)


""" Task_06_13
Создать матрицу равную разности matrix_a и matrix_b."""


matrix_dif = []
for i in range(n):
    c_list = []
    for j in range(m):
        elem = matrix_a[i][j] - matrix_b[i][j]
        c_list.append(elem)
    matrix_dif.append(c_list)


""" Task_06_14
Создать новую матрицу равную matrix_a умноженной на g. g вводится с клавиатуры"""


g = float(input("Введите число: "))
for i in range(n):
    for j in range(m):
        matrix_a[i][j] *= g
