first_list = [1, 2, 3, 5, 6]
second_list = []

# while len(first_list) != 0:
#     create_int = int(first_list[0]) * (-2)
#     second_list.append(create_int)
#     first_list.pop(0)
# print(f"Решение с while {second_list}")

#################################################
for i in range(len(first_list)):
    second_list.append(int(first_list[i]) * (-2))
print(f"Решение с for {second_list}")


