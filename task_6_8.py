from random import randint

n = 5
m = 4
g = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    g.append(h)
min_band = []
for i in range(n):
    z = 0
    for j in range(m):
        z += g[j][i]
    min_band.append(z)
an = min_band.index(min(min_band))
print("Индекс колонки с минимальной суммой элементов -", an)
