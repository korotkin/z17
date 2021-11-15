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


my_dict_variant = {
    1: [inch_to_centimeter],
    2: [centimeter_to_inch],
    3: [mile_to_km],
    4: [km_to_mile],
    5: [pounds_to_kg],
    6: [kg_to_pounds],
    7: [ounce_to_gramm],
    8: [gramm_to_ounce],
    9: [gallon_to_liter],
    10: [liter_to_gallon],
    11: [pints_to_liters],
    12: [liters_to_pints]
}

variant_of_translation = int(input("Выбирети вариант перевода (от 1 до 12): "))

while variant_of_translation != 0:
    number = int(input("Введите число для перевода: "))

    result = my_dict_variant[variant_of_translation][0](number)
    print(f"Ответ: {result}")
    variant_of_translation = int(input("Выбирети вариант перевода (от 1 до 12): "))
