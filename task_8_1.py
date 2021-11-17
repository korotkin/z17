"""
функция для создания двойного факториала
"""

def fact2 (n):
    answer=1
    if n%2==0:
        for i  in range(1,n+1):
            if i %2==0:
                answer*=i
    else:
        for i  in range(1,n+1):
            if i%2!=0:
                answer*=i
    return answer

print(fact2(6))
print(fact2(7))
