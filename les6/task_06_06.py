from random import randint
from pprint import pprint

a = int(input('Введите максимум: '))
list = []
temp_2 = []
answer = []
temp = []
count = 0
n = 0
i = 0
arr = [[randint(1, 9) for x in range(3)] for y in range(4)]
while n != len(arr[0]):
    list.clear()
    while i != 3:
        list.append(arr[i][n])
        temp_2 = list.copy()
        i += 1
    count = sum(temp_2)
    temp.append(count)
    answer = temp.index(max(temp)) + 1
    i = 0
    n += 1
print(answer)
