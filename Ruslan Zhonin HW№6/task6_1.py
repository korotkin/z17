from random import randint

arrs = input('enter the number of arrays:')
items = input('enter the number of items:')

m = range(int(arrs))
n = range(int(items))

for arr in m:
    inner_arr = []
    for i in n:
        inner_arr.append(randint(1, 25))
    print(inner_arr)
