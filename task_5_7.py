from random import randint
n=6
g=[]
for i in range(n):
    h=[]
    for j in range(n):
        v=randint(1,9)
        h.append(v)
    g.append(h)
for i in range(n):
    m = g[i].index(max(g[i]))
    for j in range(n):
        if j==i:
            g[i][j],g[i][m]=g[i][m],g[i][j]
print()
for i in g:
    print(i)