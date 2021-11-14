from random import randint

arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

matrix = []
amount = 0
for arr in m:
    inner_arr = []
    for i in n:
        item = randint(1, 25)
        inner_arr.append(item)
        amount += item
    matrix.append(inner_arr)
print(f"matrix is : {matrix}, matrix elements amount: {amount}")