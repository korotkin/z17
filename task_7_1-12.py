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
