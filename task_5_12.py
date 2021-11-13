from random import randint

a = 12
matrix = []
n = range(3)
m = range(4)
sum = 0
indexes = []
for arr in m:
    inner_arr = []
    for item in n:
        inner_arr.append(randint(0, 66))
    print(inner_arr)
    matrix.append(inner_arr)

for i, arr in enumerate(matrix):
    for j, item in enumerate(arr):
        if i == 0 and item > a:
            indexes.append(j)

for i, arr in enumerate(matrix):
    for j, item in enumerate(arr):
        if len(indexes) > 3:
            indexes.pop()
        for k in indexes:
            if j == k:
                sum += item
print(sum)
