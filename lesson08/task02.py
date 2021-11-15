"""
Задание 7.02

Написать программу для работы с матрицами:

1. Создание
2. Вывод
3. Сумма всех элементов
4. Нахождение максимального элемента
5. Нахождение минимального элемента.
"""
from random import randint

n = 10
m = 10


def get_array(a, b):
    arr = []
    for i in range(a):
        row = []
        for j in range(b):
            row.append(randint())
        arr.append(row)
    return arr


"""
min(el1, el2)  - вернет минимальный элемент
min(item_list) - вернет минимальный элемент из списка
"""


def print_array(arr):
    for row in arr:
        print(row)


def get_aray_sum(arr):
    s = 0
    for row in arr:
        s += sum(row)
    return s


def get_aray_max(arr):
    val = arr[0][0],
    for row in arr:
        val = max(val, max(row))
    return val


def get_aray_min(arr):
    val = arr[0][0],
    for row in arr:
        val = min(val, min(row))
    return val


arr = get_array(n, m)

print_array(arr)

# -------
arr_sum = get_aray_sum(arr)

arr_max = get_aray_max(arr)

arr_min = get_aray_min(arr)
