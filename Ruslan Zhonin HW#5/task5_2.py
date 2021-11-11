# Дано число. Найти сумму и произведение его цифр
number = input('enter the value: ')
figures_of_number = list(number)
sum = 0
mltpl = 1
for figure in figures_of_number:
    sum += int(figure)
    mltpl *= int(figure)
print(f"All figures of number amount: {sum}")
print(f"All figures of number multiplication: {mltpl}")

