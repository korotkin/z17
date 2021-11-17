from random import randint

m=7
n=8
g=[]
for i in range(m):
    h=[]
    for j in range(n):
        h.append(randint(1,9))
    g.append(h)
l=[]
for i in g:
    k=sum(i)
    l.append(k)
min_line=l.index(min(l))
print(min_line)