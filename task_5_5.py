from random import randint
h=[]
for i in range(20):
    h.append(randint(1,10))
g=max(h)
for item in range(len(h)):
    if h[item]% 2 == 0:
        h[item] = g
print(h)