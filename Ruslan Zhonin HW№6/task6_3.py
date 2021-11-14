from random import randint

arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

matrix = []
min_el = 25
for arr in m:
    inner_arr = []
    for i in n:
        item = randint(1, 25)
        inner_arr.append(item)
        if item < min_el:
            min_el = item
    matrix.append(inner_arr)
print(f"matrix is : {matrix}, min element in matrix: {min_el}")