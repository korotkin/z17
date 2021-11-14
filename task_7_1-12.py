#Написать 12 функций по переводу:


#1:Дюймы в сантиметры и #2:Сантиметры в дюймы
n = float(input("Введи дюймы:"))
m = float(input("Введи см:"))
def converter(n, m):
    inch = 2.54
    if m == 'duim':
        print("{} inch = {}cm ".format(n, (n * inch)))
    if m == 'cm':
        print("{} cm = {} inch ".format(n, (round(n / inch, 2))))
converter(n, 'duim')
converter(m, 'cm')


#3:Мили в километры и #4:Километры в мили

n = float(input("Введи расстояние в милях:"))
m = float(input("Введи расстояние в км:"))
def converter(n, m):
    mile = 1.60934
    if m == 'км':
        print("{} mile = {}км ".format(n, (n * mile)))
    if m == 'мили':
        print("{} км = {} mile ".format(n, (round(n / mile, 2))))
converter(n, 'км')
converter(m, 'мили')


#5:Фунты в килограммы и #6:Килограммы в фунты
n = float(input("Введи массу в кг:"))
m = float(input("Введи массу в фунтах:"))
def converter(n, m):
    funt = 2.20462
    if m == 'кг':
        print("{} фунтов = {}кг ".format(n, (n * funt)))
    if m == 'фунтов':
        print("{} кг = {} фунтов ".format(n, (round(n / funt, 2))))
converter(n, 'кг')
converter(m, 'фунтов')


#7:Унции в граммы и #8:Граммы в унции
n = float(input("Введи массу в унциях:"))
m = float(input("Введи массу в граммах:"))
def converter(n, m):
    ounce = 28.3495
    if m == 'унций':
        print("{} унций = {}грамм ".format(n, (round(n * ounce))))
    if m == 'грамм':
        print("{} грамм = {}унций ".format(n, (round(n / ounce, 2))))
converter(m, 'унций')
converter(n, 'грамм')
