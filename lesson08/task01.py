"""
Написать функцию, которая получает на вход
имя и выводит строку вида: “Hello, {name}”.
Создать список из 5 имен. Вызвать функцию
для каждого элемента списка в цикле
"""


names = ("Jack", "Ann", "Bob", "Mike", "Kate")

# Iteration 1
for name in names:
    print(name)

print('*' * 10)

# Iteration 2
for name in names:
    val = f"Hello, {name}"
    print(val)


print('*' * 10)


# Iteration 3

def my_func(name: str):
    """
    Prints user name from the parameters
    :param name: User name
    :return: None
    """
    val = f"Hello, {name}"
    print(val)

my_func('Test 123')

print('*' * 10)

for name in names:
    my_func(name)

print('*' * 10)

for name in names:
    my_func(name)

print('*' * 10)

for name in names:
    my_func(name)
