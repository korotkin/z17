"""
Задание 7.01
=============
Просуммировать  n чисел
Не учитывать числа кратные 5
Циклами  for  while c  пред и пост условиями
"""
from random import randint

arr = []
n = 10
for i in range(n):
    arr.append(randint())

i = len(arr) - 1
s = 0
while i >= 0:
    if arr[i] % 5 == 0:
        s += arr[i]
    i -= 1

print(f"SUM={s}")


i = len(arr) - 1
s = 0
while True:
    if arr[i] % 5 == 0:
        s += arr[i]
    i -= 1
    if i < 0:
        break
print(f"SUM={s}")


s = 0
for el in arr:
    if el % 5 == 0:
        s += el

s = sum([el for el in arr if el % 5 == 0])
