from random import randint

g=int(input('введите G'))
m=7
n=8
matrix_a=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    matrix_a.append(h)
answer=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(matrix_a[i][j]*g)
    answer.append(h)
for i in answer:
    print(i)