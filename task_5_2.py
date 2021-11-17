number=input('введите число = ')
list_number=[int(x) for x in number]
summa=sum(list_number)
proizvedenie=1
for elem in list_number:
    proizvedenie*=elem
print(summa)
print(proizvedenie)


