"""
Задание 7.03
=============
"""

arr = [1, 2, 3, 1, 2, 1, 6, 7, 8, 1, 8, 2, 5, 6, 7]

new_arr = []
for el in arr:
    if el not in new_arr:
        new_arr.append(el)







def my_func(a, b):
    summ = a + b
    print(f'{a} + {b} = {summ}')


my_func(4, 5)
my_func(a=4, b=5)


def my_func(a, b=10):
    summ = a + b
    print(f'{a} + {b} = {summ}')


my_func(4)
my_func(a=4)





def my_func(a, b=10):
    c = a + b
    print(c)


def my_func(a, b=10):
    return


def my_func(a, b):
    summ = a + b
    return  summ


my_func(4, 5)
my_func(a=4, b=5)
my_func(b=6, a=4)


def my_func(a, b=5):
    summ = a + b
    return summ

my_func(a=4)
my_func(4)