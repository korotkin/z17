first_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
all_keys = list(first_dict.keys())
val = list(first_dict.values())
second_dict = {}
third_dict = {}
counter = 0

# while counter != len(all_keys):
#     length_of_key = len(all_keys[counter])
#     new_key = all_keys[counter] + str(length_of_key)
#     second_dict[new_key] = val[counter]
#     counter += 1
# print(f"Решение с while {second_dict}")

################################################

for key, values in first_dict.items():
    print(first_dict[key])
    length_of_key = len(key)
    new_key = key + str(length_of_key)
    third_dict[new_key] = values
print(f"Решение с for {third_dict}")