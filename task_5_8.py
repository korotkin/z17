my_list = "one two three four five six seven eight nine ten".split()
new_list = []
for i in my_list:
    new_list.append(i)
    new_list.append('')
new_list = new_list[:-1]
print(*reversed(my_list))
