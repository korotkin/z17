from random import randint

m=7
n=8
g=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    g.append(h)
min_band=[]
for i in range(n):
    p=0
    for j in range(m):
        p+=g[j][i]
    min_band.append(p)
answer=min_band.index(min(min_band))
print(answer)