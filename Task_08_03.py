"""
Task_08_03
Описать функцию Sin1( x , ε ) вещественного типа (параметры x , ε —
вещественные, ε > 0), находящую приближенное значение функции sin( x ):
sin( x ) = x – x ^3 /(3!) + x^ 5 /(5!) – ... + (–1) ^ n · x^( 2·n+1) /((2· n +1)!) + ... .
В сумме учитывать все слагаемые, модуль которых больше ε
"""

from math import factorial, fabs


def sin1(x, e):
    n = int(input("Введите степень ряда n: "))
    result = 0
    for i in range(0, n + 1):
        sin_x = (-1) ** i * x ** (2 * i + 1) / (factorial(2 * i + 1))
        if fabs(sin_x) > e:
            result += sin_x
    return result


