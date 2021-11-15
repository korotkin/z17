"""Task_07_01
Написать 12 функций по переводу:
1. Дюймы в сантиметры
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
Примечание: функция принимает на вход число и возвращает конвертированное число"""


def inch_to_centimeter(number):
    result = number * 2.54
    return result


def centimeter_to_inch(number):
    result = number * 0.39
    return result


def mile_to_km(number):
    result = number * 1.6
    return result


def km_to_mile(number):
    result = number * 0.62
    return result


def pounds_to_kg(number):
    result = number * 0.45
    return result


def kg_to_pounds(number):
    result = number * 2.2
    return result


def ounce_to_gramm(number):
    result = number * 28.35
    return result


def gramm_to_ounce(number):
    result = number * 0.035
    return result


def gallon_to_liter(number):
    result = number * 3.78
    return result


def liter_to_gallon(number):
    result = number * 0.26
    return result


def pints_to_liters(number):
    result = number * 0.57
    return result


def liters_to_pints(number):
    result = number * 1.76
    return result
