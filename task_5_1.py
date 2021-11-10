print("Ноль в качестве знака,завершит работу программы")
while True:
    s = input("Введи знак:(+, –, /, *)")
    if s == '0':
        break
    if s in ('+', '-', '/', '*'):
        x = float(input("Введи число #1:"))
        y = float(input("Ввдеи число#2:"))
        if s == '+':
            z = x + y
            print(z)
        elif s == '-':
            z = x - y
            print(z)
        elif s == '*':
            z = x * y
            print(z)
        elif s == '/':
            if y != 0:
                z = x / y
                print(z)
            else:
                print("Деление на ноль!")
    else:
        print("Неверный знак")
