from random import randint

m=7
n=8
g=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    g.append(h)
for i in range(m):
    for j in range(n):
        if i>j:
            g[i][j]=0
for i in g:
    print(i)