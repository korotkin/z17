from random import randint

n = 3
m = 3

matrix_a = []
for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(1, 100)
        arr1.append(p)
    matrix_a.append(arr1)

print(matrix_a)

matrix_b = []
for i in range(n):
    arr2 = []
    for j in range(m):
        p = randint(1, 100)
        arr2.append(p)
    matrix_b.append(arr2)

print(matrix_b)

matrix_sum = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
for x in matrix_sum:
    print(x)

matrix_min = [[matrix_a[i][j] - matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
for y in matrix_min:
    print(y)

g = input()
g = []
matrix_a1 = matrix_a * g


print(matrix_a1)
