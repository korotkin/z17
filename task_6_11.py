from random import randint

n = 5
m = 4
matrix_a = []
for i in range(m):
    a = []
    for j in range(n):
        a.append(randint(1, 66))
    matrix_a.append(a)
    print("Матрица 1:", a)

n = 5
m = 4
matrix_b = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    matrix_b.append(h)
    print("Матрица 2: ", h)
