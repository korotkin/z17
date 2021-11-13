from random import randint

g = int(input('Input G'))
n = 5
m = 4
matrix_a = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    matrix_a.append(h)
answer = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(matrix_a[i][j]*g)
    answer.append(h)
for i in answer:
    print(i)
