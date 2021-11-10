val = [100, 233, 35, 4343, 544]

x = val[-1]
for i, y in enumerate(val):
    val[i], x = x, y

print(val)
