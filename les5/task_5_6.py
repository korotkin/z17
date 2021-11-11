count = 0
a = [1, 2, 5, 4, 3, 2, 3, 10, 5, 4, 2, 3, 4, 5]
length = len(a)

for j in range(length - 1):
    if a[j + 1] < a[j] and a[j] > a[j - 1]:
        if a[j] > a[j - 1]:
            count += 1
    elif j + 2 == length:
        count += 1
print(f"Количество {count}")
