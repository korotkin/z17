task = """1. Дюймы в сантиметры
2. Сантиметры в дюймы
3. Мили в километры
4. Километры в мили
5. Фунты в килограммы
6. Килограммы в фунты
7. Унции в граммы
8. Граммы в унции
9. Галлон в литры
10. Литры в галлоны
11. Пинты в литры
12. Литры в пинты
0. Выход"""


print('Калькулятор')


def calс(param, val):
    if param == 1:
        print(val * 2.54)
    elif param == 2:
        print(val * 0.394)
    elif param == 3:
        print(val * 0.62)
    elif param == 4:
        print(val * 1.6)
    elif param == 5:
        print(val * 0.45)
    elif param == 6:
        print(val * 2.2)
    elif param == 7:
        print(val * 28.34)
    elif param == 8:
        print(val * 0.035)
    elif param == 9:
        print(val * 0.26)
    elif param == 10:
        print(val * 3.79)
    elif param == 11:
        print(val * 0.568)
    elif param == 12:
        print(val * 1.76)

print(task)
while True:
    parameter = int(input('Введите нужный параметр:'))
    if parameter == 0:
        break
    elif parameter > 12:
        print('Неверное значение параметра')
    else:
        value = int(input("Введите число: "))
        calс(parameter, value)