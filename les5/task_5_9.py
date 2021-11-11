from pprint import pprint
from random import randint


list_of_del = []
any_list = []
new_dict = {}

m = int(input("input M: "))
n = int(input("input N: "))

for i in range(m, n + 1):
    list_of_del.clear()
    for j in range(1, i + 1):
        if i % j == 0 and j != i and j != 1:
            list_of_del.append(j)
            any_list = list_of_del.copy()
            new_dict.update({i: any_list})
pprint(new_dict)



