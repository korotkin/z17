from random import randint

i = 0
n = -1
iter = 0
maximum = 0
# a = [randint(1, 50) for j in range(19)]
a = [40, 2, 3, 5, 3, 30, 1, 4, 10]
print(a)
while i != len(a):
    if (a[n] > a[n + 1]) and (a[n] > maximum):
        maximum = a[n]
    n += 1
    i += 1
print(maximum)
while iter != len(a):
    if a[iter] % 2 == 0:
        a[iter] = maximum
    iter += 1
print(a)