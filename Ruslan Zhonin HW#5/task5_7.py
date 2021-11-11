# Дана целочисленная квадратная матрица.
# Найти в каждой строке наибольший элемент и поменять его местами с элементом главной диагонали.

matrix = [[1,2,3,8], [4,5,6,3], [7,8,9,7], [2,5,7,4]]

for i, arr in enumerate(matrix):
    maximum = 0
    for item in arr:
       if item > maximum:
           maximum = item
    for j in arr:
        arr[i] = maximum
    print(arr)