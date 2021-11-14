from random import randint

arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

matrix = []
max_amount = 0
row_index = 0
for ind, arr in enumerate(m):
    amount = 0
    inner_arr = []
    for i in n:
        item = randint(1, 25)
        inner_arr.append(item)
        amount += item
    if amount > max_amount:
        max_amount = amount
        row_index = ind
    matrix.append(inner_arr)
print(f"matrix is : {matrix}, max amount row index: {row_index}")