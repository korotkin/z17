#  В массиве целых чисел с количеством элементов 19 определить максимальное
# число и заменить им все четные по значению элементы.
from random import randint
arr = []
maximum = 0
for i in range(0, 19):
    arr.append(randint(1, 20))
for item in arr:
    if item > maximum:
        maximum = item
for i, item in enumerate(arr):
    if i%2 == 0:
        arr[i] = maximum
print(f"maximum is: {maximum}")
print(arr)
