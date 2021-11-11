from random import randint
from pprint import pprint

n = int(input("N: "))
count = 0
list = []
answer = []

a = [[randint(1, 9) for x in range(n)] for y in range(n)]
print(a)

for i in a:
    count = sum(i)
    list.append(count)
    answer = list.index(max(list)) + 1

pprint(answer)
