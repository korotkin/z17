from random import randint

m=7
n=8
max=9
g=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,max))
    g.append(h)
h=max
for i in range(m):
    for j in range(n):
        if g[i][j]<h:
            h=0
            h=g[i][j]
print(h)