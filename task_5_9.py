num1 = int(input("Введи число 1:"))
num2 = int(input("Введи число 2:"))
val = range(num1, num2)
for i in val:
    list = []
    for e in range(2, i - 1):
        if i % e == 0:
            list.append(str(e))
    delitel = " ".join(list)
    print(f'{i}:{delitel}')
