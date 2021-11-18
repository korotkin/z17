"""
Task_08_01
Описать функцию fact2( n ), вычисляющую двойной факториал :n!! =
1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное (n > 0 —
параметр целого типа. С помощью этой функции найти двойные
факториалы пяти данных целых чисел
"""

def fact2(n):
    if n % 2 == 0:
        factorial = 2
        if n != 2:
            for i in range(4, n + 1, 2):
                factorial *= i
            return factorial
        else:
            return factorial
    else:
        factorial = 1
        if n != 1:
            for i in range(1, n + 1, 2):
                factorial *= i
            return factorial
        else:
            return factorial


numbers = [5, 6, 8, 9, 10]
for num in numbers:
    result = fact2(num)
    print(result)

