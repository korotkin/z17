new_list = [1, 2, 3, 5, 6, 8]
counter = 0
new_counter = 0

# while len(new_list) != 0:
#     first_number = new_list[0]
#     if first_number % 2 == 0:
#         counter += 1
#     new_list.pop(0)
# print(f"Решение с while {counter}")

##########################################

for i in range(len(new_list)):
    int_num = new_list[i]
    if int_num % 2 == 0:
        new_counter += 1
print(f"Решение с for {new_counter}")
