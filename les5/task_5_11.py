from random import randint

n = int(input('Введите максимум: '))
count = 0
i = 0
j = 0

arr = [[randint(1, 9) for x in range(n)] for y in range(n)]
while i != n:
    while j != n:
        count += sum(arr[i][j + 1:])
        i += 1
        j += 1

print(f'Сумма равна {count}')
