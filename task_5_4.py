n = int(input("Введите заданное число n="))
print("Сумма чисел от 1 до", n, "=", sum([i for i in range(1, n + 1)]))

task_5_5.py

list_me = []
a = 0
from random import randint
while a < 19:
    list_me.append(randint(0,200))
    a += 1
list_me = list(map(lambda x: max(list_me) if x % 2 == 0 else x, list_me))
