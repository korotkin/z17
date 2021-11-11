"""
Задание 7.03
=============
Найти второй максимальный элемент массива
arr = [1,2,3,1,2,1,6,7,8,1,8,2,5,6,7]
"""
arr = [1,2,3,1,2,1,6,7,8,1,8,2,5,6,7]

max_el = arr[0]
el2_ind = 1
for i, el in enumerate(arr):
    if i == 0:
        continue
    if el > max_el:
        max_el = el
    elif el == max_el:
        el2_ind = i
print (el2_ind)


