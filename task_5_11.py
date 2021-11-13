# сумма элементов выше главной диагонали массива nxn

matrix_1 = [[55, 2, 34, 8], [4, 66, 6, 34], [74, 8, 123, 7], [2, 663, 7, 0]]

sum = 0
for i, arr in enumerate(matrix_1):
    for j, item in enumerate(arr):
        if j > i:
            sum += item
print(sum)
