import math
math.hypot
x = float(input("Введите катет 1:"))
y = float(input("Введите катет 2:"))
sqrt = math.sqrt(x**2+y**2)
print("Гипотенуза прямоугольного треульника равна:")
print(sqrt)

x = float(input("Введите катет 1:"))
y = float(input("Введите катет 2:"))
sqrt = x*y/2
print("Площадь прямоугольного треульника равна:")
print(sqrt)

exit = print(input("Нажмите Enter для выхода"))
