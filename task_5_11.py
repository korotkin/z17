from random import randint
n=6
g=[]
sum=0
for i in range(n):
    h=[]
    for j in range(n):
        v=randint(1,9)
        h.append(v)
    g.append(h)
for i in g:
    print(i)
for i in range(n):
    for j in range(n):
        if i<j:
            sum+=g[i][j]

print(sum)