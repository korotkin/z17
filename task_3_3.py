data_in = input("Введите число: ")

len_data_in = len(data_in)

if len_data_in > 10:
    data_in += "!!!"
    print(data_in)
else:
    data_in_second = data_in[1]
    print(data_in_second)