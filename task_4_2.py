my_numbers = [1, 10, 6, 45, 98, 11, 51, 42, 65]
even_numbers = 0
for i in my_numbers:
    if (i % 2) == 0:
        even_numbers += 1

print('Number of even numbers', even_numbers)
