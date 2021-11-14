from random import randint
import math
arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

matrix = []
min_amount = math.inf
row_index = 0
for ind, arr in enumerate(m):
    amount = 0
    inner_arr = []
    for i in n:
        item = randint(1, 25)
        inner_arr.append(item)
        amount += item
    print(amount)
    if amount < min_amount:
        min_amount = amount
        row_index = ind
    matrix.append(inner_arr)
print(f"min amount: {min_amount}")
print(f"matrix is : {matrix}, min amount row index: {row_index}")