from random import randint

a = int(input('Введите максимум: '))
count = 0
n = 0
i = 0
arr = [[randint(1, 9) for x in range(3)] for y in range(4)]

while n != len(arr[0]):
    if arr[0][n] > a:
        while i != 4:
            count += arr[i][n]
            i += 1
        i = 0
        n += 1
    else:
        n += 1

print(f'Сумма равна {count}')
