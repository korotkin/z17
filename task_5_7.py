from random import randint

matrix_1 = []
n = int(input('Enter n:'))
m = int(input('Enter m:'))

matrix = [[randint(10, 90) for j in range(n)] for i in range(m)]
print(*matrix)
for i in range(min(n, m)):
    r = matrix[i].index(max(matrix[i]))
    matrix[i][i], matrix[i][r] = matrix[i][r], matrix[i][i]
print(*matrix)
