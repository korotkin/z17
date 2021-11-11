
any_list = []
answer = []
keys = []
values = []
list_of_del = []
new_dict = {}
summary = 0
n = 0

for i in range(200, 300):
    list_of_del.clear()
    for j in range(1, i + 1):
        if i % j == 0 and j != i:
            list_of_del.append(j)
            summary = sum(list_of_del)
    any_list.append(summary)
    new_dict.update({i: summary})
for key, v in new_dict.items():
    keys.append(key)
    for value in new_dict.values():
        values.append(value)
        while n != len(values):
            if key == values[n] and new_dict.get(v, 0) == key:
                answer.append(key)
            n += 1

print(answer)
