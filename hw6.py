from random import randint

n = 4
m = 4

a = int(input())
b = int(input())

arr = []
for i in range(n):
    arr1 = []
    for j in range(m):
        p = randint(a, b)
        arr1.append(p)
    arr.append(arr1)

def print_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=' ')
        print()

print_matrix(arr)

num = []
for k in arr:
    for i in k:
        num.append(i)

print('Максимальный элемент - ', max(num))
print('Минимальный элемент - ', min(num))

summa = 0
for i in range(n):
    for j in range(m):
        summa += arr[i][j]
print('Сумма элементов матрицы:', summa)

sum_max = 0
sum_min = 0
str_max = 0
col_max = 0
str_min = 0
col_min = 0
for i in range(n):
    s = 0
    for j in range(m):
        s += arr[i][j]
        if s > sum_max:
            sum_max = s
            str_max = j
            col_max = i
            if s < sum_min:
                sum_min = s
                str_min = j
                col_min = i

print('Индекс масксимального ряда - ', str_max)
print('Индекс максимальной колонки -', col_max)
print('Индекс минимального ряда - ', str_min)
print('Индекс минимального ряда - ', str_min)

arr2 = []
for i in range(n):
    for j in range(m):
        if i < j:
            arr[i][j] = 0
print_matrix(arr)

for i in range(n):
    for j in range(m):
        if i > j:
            arr[i][j] = 0
print_matrix(arr)



