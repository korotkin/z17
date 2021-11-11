# Написать программу, в которой вводятся два операнда Х и Y и знак операции
# sign (+, –, /, *). Вычислить результат Z в зависимости от знака. Предусмотреть
# реакции на возможный неверный знак операции, а также на ввод Y=0 при
# делении. Организовать возможность многократных вычислений без перезагрузки
# программа (т.е. построить бесконечный цикл). В качестве символа прекращения
# вычислений принять ‘0’ (т.е. sign='0').

while True:
    print('start to enter values, enter 0 as a sign to stop')
    x = input('Enter x: ')
    y = input('Enter Y: ')
    sign = input('Enter operand: ')
    if sign == '0':
        break
    elif sign == '/' and y == '0':
        print('Incorrect value or sign')
    elif sign == '+':
        z = int(x) + int(y)
        print(f"result: {z}")
    elif sign == '-':
        z = int(x) - int(y)
        print(f"result: {z}")
    elif sign == '*':
        z = int(x) * int(y)
        print(f"result: {z}")
    elif sign == '/':
        z = int(x) / int(y)
        print(f"result: {z}")
    else:
        print('Incorrect sign')