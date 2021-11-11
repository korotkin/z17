# сумма элементов выше главной диагонали массива nxn

matrix = [[1,2,3,8], [4,5,6,3], [7,8,9,7], [2,5,7,4]]

sum = 0
for i, arr in enumerate(matrix):
    for j, item in enumerate(arr):
        if j > i:
            sum += item
print(sum)