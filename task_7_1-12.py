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
