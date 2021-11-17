import math

a = int(input("Введите a: "))
b = int(input("Введите c: "))
c = int(input("Введите b: "))

d = b ** 2 - 4 * a * c

if a == 0 or b == 0 or c == 0:
    print("Коэффициенты равны нулю")
elif d < 0:
    print("Корней нет")
elif d == 0:
    x = -b / 2 * a
    print(f"Корень один: {x}")
else:
    first_x = (-b + math.sqrt(d)) / (2 * a)
    second_x = (-b - math.sqrt(d)) / (2 * a)
    print(f"Первый корень {first_x}, второй корень {second_x}")