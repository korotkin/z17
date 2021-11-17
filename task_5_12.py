from random import randint
a=2
n=4
m=3
g=[]
for i in range(n):
    h=[]
    for j in range(m):
        v=randint(1,9)
        h.append(v)
    g.append(h)
for i in g:
    print(i)
for j in range(m):
    sum_elem=0
    if g[0][j]>a:
        for i in range(n):
            sum_elem+=g[i][j]
    print(sum_elem)
