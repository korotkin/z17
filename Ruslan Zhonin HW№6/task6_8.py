from random import randint
import math

arrays = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrays))
n = range(int(items))

matrix = []
min_amount = math.inf
min_col_ind = 0
for ind, arr in enumerate(m):
    inner_arr = []
    for i in n:
        item = randint(1, 25)
        inner_arr.append(item)
    print(inner_arr)
    matrix.append(inner_arr)
col_ind = len(matrix)
for ind, k in enumerate(n):
    col_amount = 0
    for arr in matrix:
        for i, item in enumerate(arr):
            if i == col_ind:
                col_amount += arr[col_ind]
        if col_amount < min_amount:
            min_amount = col_amount
            min_col_ind = ind
    print(col_amount)
    col_ind -= 1
print(f"min: {min_amount}")
print(f"matrix is : {matrix}, min amount column index: {min_col_ind}")