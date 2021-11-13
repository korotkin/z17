from random import randint

n = 5
m = 4
g = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    g.append(h)
max_band = []
for i in range(n):
    z = 0
    for j in range(m):
        z += g[j][i]
    max_band.append(z)
answer = max_band.index(max(max_band))
print(answer)
