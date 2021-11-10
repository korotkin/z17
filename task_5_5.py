list_me = []
a = 0
from random import randint
while a < 19:
    list_me.append(randint(0,200))
    a += 1
list_me = list(map(lambda x: max(list_me) if x % 2 == 0 else x, list_me))
print(*list_me)
