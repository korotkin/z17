list_of_num = [1, 1]
counter = 2
x = y = 1

# while len(list_of_num) != 15:
#     summary = list_of_num[counter - 1] + list_of_num[counter - 2]
#     list_of_num.append(summary)
#     counter += 1
# print(f"Решение с while {list_of_num}")

############################################

for i in range(1, 14):
    x, y = y, x + y
    print(f"Решение с for {y}")