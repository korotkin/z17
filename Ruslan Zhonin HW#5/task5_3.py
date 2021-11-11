# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.
import math
inserted_range = range(200, 301)
pairs_list = []
for value in inserted_range:
    dividers_list = []
    for i in range(1, value):
        if value % i == 0 and i != value:
            dividers_list.append(i)
    sum1 = math.fsum(dividers_list)

    if 200 <= sum1 <= 300:
        dividers_list1 = []
        for j in range(1, int(sum1)):
            if value % j == 0 and j != value:
                dividers_list1.append(j)
        sum2 = math.fsum(dividers_list1)
        if sum2 == value:
            print('check')
            pairs_list.append(value)
print(pairs_list)
