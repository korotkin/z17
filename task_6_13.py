from random import randint

m=7
n=8
matrix_a=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    matrix_a.append(h)
m=7
n=8
matrix_b=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    matrix_b.append(h)
answer=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(matrix_a[i][j]-matrix_b[i][j])
    answer.append(h)
for i in answer:
    print(i)