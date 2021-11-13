from random import randint

n = 5
m = 4
g = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    g.append(h)
l = []
for i in g:
    k = sum(i)
    l.append(k)
min_line = l.index(min(l))
print("Минимальная сумма элементов -", min_line)
