from random import randint

m=7
n=8
g=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    g.append(h)
max_band=[]
for i in range(n):
    p=0
    for j in range(m):
        p+=g[j][i]
    max_band.append(p)
answer=max_band.index(max(max_band))
print(answer)