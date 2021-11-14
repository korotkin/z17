#  Обнулить все элементы матрицы выше главной диагонали.

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
