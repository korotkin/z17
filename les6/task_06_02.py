from random import randint
from pprint import pprint
top = 0
n = int(input("N: "))
m = int(input("M: "))

arr = [[randint(1, 9) for x in range(n)] for y in range(m)]

pprint(arr)

for i in arr:
    for j in i:
        if j > top:
            top = j
print(top)