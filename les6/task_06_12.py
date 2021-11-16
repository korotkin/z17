from random import randint
from pprint import pprint

n = int(input("N: "))
m = int(input("M: "))
#
# matrix_a = [[randint(1, 9) for x in range(n)] for y in range(m)]
# matrix_b = [[randint(1, 9) for i in range(n)] for j in range(m)]
matrix_res = [[0 for k in range(n)] for l in range(m)]
print(matrix_res)

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

for i in range(len(matrix_a)):
    for k in range(len(matrix_b)):
        matrix_res[i][k] = matrix_a[i][k] + matrix_b[i][k]

print(matrix_res)