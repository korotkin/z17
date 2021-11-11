from random import randint
from pprint import pprint

n = int(input("N: "))
m = int(input("M: "))

matrix_a = [[randint(1, 9) for x in range(n)] for y in range(m)]
matrix_b = [[randint(1, 9) for i in range(n)] for j in range(m)]
matrix_res = [[0 for i in range(n)] for k in range(m)]
print(matrix_res)


for i in range(len(matrix_a)):
    for k in range(len(matrix_b)):
        matrix_res[i][k] = matrix_a[i][k] - matrix_b[i][k]

print(matrix_res)