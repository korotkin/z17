data_in = input("Введите строку: ")

if len(data_in) % 2 == 0:
    print("Введите нечетную сроку")
else:
    center_data_in = int(len(data_in) / 2)
    letter = data_in[center_data_in]
    print(f"Центральная буква {letter}")
    if data_in.startswith(letter):
        result = data_in[1:-1]
        print(result)