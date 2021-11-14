from random import randint

arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

matrix_a = []
matrix_b = []
for arr in m:
    inner_arr_a = []
    inner_arr_b = []
    for i in n:
        item_a = randint(1, 25)
        item_b = randint(1, 25)
        inner_arr_a.append(item_a)
        inner_arr_b.append(item_b)
    matrix_a.append(inner_arr_a)
    matrix_b.append(inner_arr_b)

print(f"matrix a: {matrix_a}\nmatrix b: {matrix_b}")