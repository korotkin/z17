from random import randint

n = int(input('Введите максимум: '))
count = 0
i = 0
j = 0
arr = [[randint(1, 9) for x in range(n)] for y in range(n)]
print(arr)
while i != n:
    while j != n:
        length = len(arr[i][0: j])
        arr[i][0: j] = [0] * length
        i += 1
        j += 1

print(f'Сумма равна {arr}')
