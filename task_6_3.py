from random import randint

n = 5
m = 4
max = 66
g = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, max))
    g.append(h)
h = max
for i in range(m):
    for j in range(n):
        if g[i][j] < h:
            h = 0
            h = g[i][j]
print(h)	
