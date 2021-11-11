from random import randint
from pprint import pprint
n = int(input("N: "))
count = 0

a = [[randint(1, 9) for x in range(n)] for y in range(n)]
print(a)

for i in a:
    for j in i:
        count += j
print(f"Количество {count}")