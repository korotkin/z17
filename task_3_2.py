num = int(input("Введи кол-во людей"))
if num > 50:
    print(f"Ресторан - {num}")
if 20 <= num < 50:
    print(f"Кафэ - {num}")
if num < 20:
    print(f"Дома - {num}")
else:
    pass
