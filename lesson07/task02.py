"""
Задание 7.02
=============
Python: Вывести значение квадратов индексов элементов  в массиве 1-30 исключая первые 5 элементов
Python: Generate and print a list except for the first 5 elements, where the values are square of numbers between two numbers
"""
l = list()
for i in range(1, 31):
    if i > 5:
        l.append(i ** 2)
    # l.append((i > 5 and i ** 2) or i)
    #  1 элемент
    #  (false) (1)
    #  6 элемент
    #  (36) игнор
print(l)

############

arr = range(1, 31)
new_arr = []
for i in arr:
    if i > 5:
        new_arr.append(i ** 2)

print(new_arr)
