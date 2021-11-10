num = int(input("Введите число"))

sum = 0
mul = 1

while num > 0:
    digit = num % 10
    sum = sum + digit
    mul = mul * digit
    num = num // 10

print("Сумма:", sum)
print("Произведение:", mul)
