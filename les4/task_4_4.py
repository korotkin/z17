new_dict = [1, 2, 3, 4, 5]
# first_num = new_dict[0]

# while first_num != new_dict[-1]:
#     plus = new_dict.pop(0)
#     new_dict.append(plus)
# print(f"Решение с while {new_dict}")

####################################################

for i in range(1):
    plus = new_dict[i]
    print(plus)
    new_dict.append(plus)
    new_dict.pop(i)
print(f"Решение с while {new_dict}")
