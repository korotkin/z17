from random import randint

arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

matrix_a = []
matrix_b = []
matrix_c = []
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

for i, arr in enumerate(m):
    inner_arr_c = []
    for j, item in enumerate(n):
        inner_arr_c.append(matrix_a[i][j] + matrix_b[i][j])
    matrix_c.append(inner_arr_c)

print(f"matrix c: {matrix_c}")
