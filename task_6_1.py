from random import randint

n = 5
m = 4
g = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    g.append(h)
for i in g:
    print(i)
