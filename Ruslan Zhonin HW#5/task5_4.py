# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число

n = input('insert a number: ')
s = 0
for i in range(1, int(n) + 1):
    s += float(1 / i)
print(s)