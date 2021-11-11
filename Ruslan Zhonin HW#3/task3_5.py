#task5
from math import sqrt
print('solve the quadratic equation ax^2 + bx + c = 0')
a = float(input('enter the value of a = '))
b = float(input('enter the value of b = '))
c = float(input('enter the value of c = '))

discr = b**2 - 4 * a * c
print(f"discriminant is = {discr}")

if discr > 0:
    first_x = (-b + sqrt(discr)) / (2 * a)
    second_x = (-b - sqrt(discr)) / (2 * a)
    print(f"first root={first_x}  second root={second_x}")
elif discr == 0:
    x = -b / (2 * a)
    print(f"root={x}")
else:
    print('There are no roots')





