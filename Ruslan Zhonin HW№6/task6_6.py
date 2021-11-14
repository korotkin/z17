from random import randint

arrays = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrays))
n = range(int(items))

matrix = []
max_amount = 0
max_col_ind = 0
for ind, arr in enumerate(m):
    inner_arr = []
    for i in n:
        item = randint(1, 25)
        inner_arr.append(item)
    print(inner_arr)
    matrix.append(inner_arr)
col_ind = 0
for ind, k in enumerate(n):
    col_amount = 0
    for arr in matrix:
        for i, item in enumerate(arr):
            if i == col_ind:
                col_amount += arr[col_ind]
        if col_amount > max_amount:
            max_amount = col_amount
            max_col_ind = ind
    print(col_amount)
    col_ind += 1
print(f"max: {max_amount}")
print(f"matrix is : {matrix}, max amount column index: {max_col_ind}")