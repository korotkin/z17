from random import randint

arrs = input('enter the number:')

m = range(int(arrs))

matrix = []
for arr in m:
    inner_arr = []
    for i in m:
        item = randint(1, 25)
        inner_arr.append(item)
    matrix.append(inner_arr)

for i, arr in enumerate(matrix):
    for j, item in enumerate(arr):
        if j > i:
            arr[j] = 0
    print(arr)