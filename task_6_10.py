from random import randint

n = 5
m = 4
z = []
for i in range(m):
    h = []
    for j in range(n):
        h.append(randint(1, 66))
    z.append(h)
for i in range(m):
    for j in range(n):
        if i > j:
            z[i][j] = 0
for i in z:
    print(i)
