from random import randint
print("Сумма двух матриц:")
n = 5
m = 4
matrix_a = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    matrix_a.append(h)
n = 5
m = 4
matrix_b = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    matrix_b.append(h)
answer = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(matrix_a[i][j]+matrix_b[i][j])
    answer.append(h)
for i in answer:
       print(i)
