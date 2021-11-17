data_in = int(input("Введите возраст: "))

if data_in > 50:
    print("ресторан")
elif 20 < data_in < 50:
    print("кафе")
else:
    print("дом")