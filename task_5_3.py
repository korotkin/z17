f = 0
for num in range(200, 300):
    if num != f:
        s1 = 0
        for i in range(1, num // 2 + 1):
            if num % i == 0:
                s1 += i
        s2 = 0
        for j in range(1, s1 // 2 + 1):
            if s1 % j == 0:
                s2 += j
        if s2 == num != s1:
            print(num, s1)
            f = s1
