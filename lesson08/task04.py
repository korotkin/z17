"""
Задание 7.04

a. Реализовать функцию возвращающую
матрицу. На вход принимает n - размерность
матрицы, random_from(по-умолчанию 1),
random_to(по-умолчанию(9)).

б. изменить функцию, так чтобы она получала параметры из **kwargs
"""

from random import randint


# Решение А.
def matrix(n, random_from=1, random_to=9):
    matrix_a = []
    for i in range(n):
        h = []
        for j in range(n):
            h.append(randint(random_from, random_to))
        matrix_a.append(h)
    return matrix_a


print(matrix(10, ))
print(matrix(10, random_from=2, random_to=20))
print(matrix(10, random_to=20))
print(matrix(10, random_from=2))
print(matrix(10, random_from=2))
print(matrix(10, 1, 200))


# Решение Б.
"""
*args    - arguments
*kwargs  - key value arguments
"""


def matrix1(n, **kwargs):
    matrix_a = []
    # random_from = kwargs.get('random_from', 1)
    # random_to = kwargs.get('random_to', 9)
    for i in range(n):
        h = []
        for j in range(n):
            h.append(randint(kwargs['random_from'], kwargs['random_to']))
            # h.append(randint(random_from, random_to))
        matrix_a.append(h)
    return matrix_a


print(matrix1(10, random_from=2, random_to=20))
print(matrix1(10, random_to=20))
print(matrix1(10, random_from=2))
print(matrix1(10, random_from=2))
