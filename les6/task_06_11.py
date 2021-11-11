from random import randint
from pprint import pprint

n = int(input("N: "))
m = int(input("M: "))

matrix_a = [[randint(1, 9) for x in range(n)] for y in range(m)]
matrix_b = [[randint(1, 9) for i in range(n)] for j in range(m)]

print(matrix_a, matrix_b)