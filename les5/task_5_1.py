

list_of_sign = ["+", "-", "/", "*"]
while True:
    x = float(input("input x: "))
    y = float(input("input y: "))
    sign = input("sign: ")
    if sign == "+":
        z = x + y
        print(f"Ответ {z}")
        break
    elif sign == "-":
        z = x - y
        print(f"Ответ {z}")
        break
    elif sign == "/" and y != 0:
        z = x / y
        print(f"Ответ {z}")
        break
    elif sign == "*":
        z = x * y
        print(f"Ответ {z}")
        break
    elif y == 0:
        print("Введите не  0!")
    elif sign not in list_of_sign:
        print("Введена неверная операция!")
    else:
        if input("Продолжим (Y/N) ") != "0":
            print("Выход из программы!")
            break

