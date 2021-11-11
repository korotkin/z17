from random import randint
from pprint import pprint
n = int(input("N: "))


a = [[randint(1, 100) for x in range(n)] for y in range(n)]
print(a)
min = a[0][0]

for i in range(n):
    for j in range(n):
        if a[i][j] < min:
            min = a[i][j]
print(f"Количество {min}")