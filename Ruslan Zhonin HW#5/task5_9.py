# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

m = input('enter the start of range: ')
n = input('enter the end of range: ')

inserted_range = range(int(m), int(n))

for value in inserted_range:
    dividers_list = []
    for i in range(2, value):
        if value%i == 0 and i != value:
            dividers_list.append(i)
    print(f"{value}: {dividers_list}")
