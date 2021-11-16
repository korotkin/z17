from random import randint
from pprint import pprint

n = int(input("N: "))
m = int(input("M: "))
g = int(input("G: "))
matrix_a = [[randint(1, 9) for x in range(n)] for y in range(m)]
matrix_res = [[0 for i in range(n)] for k in range(m)]

print(matrix_a)


for i in range(len(matrix_a)):
    for k in range(len(matrix_a)):
        matrix_res[i][k] = matrix_a[i][k] * g

print(matrix_res)