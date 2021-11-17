x=int(input('введите X = '))
y=int(input('введите Y = '))
sing=(input('введите знак = '))
while sing!=0:
    if sing=='/':
        if y!=0:
            z=x/y
            print(z)
            x = int(input('введите X = '))
            y = int(input('введите Y = '))
            sing = (input('введите знак = '))
        else:
            print('на ноль делить нельзя')
            x = int(input('введите X = '))
            y = int(input('введите Y = '))
            sing = (input('введите знак = '))

    elif sing=='+':
        z=x+y
        print(z)
        x = int(input('введите X = '))
        y = int(input('введите Y = '))
        sing = (input('введите знак = '))
    elif sing=='-':
        z=x-y
        print(z)
        x = int(input('введите X = '))
        y = int(input('введите Y = '))
        sing = (input('введите знак = '))
    elif sing=='*':
        z=x*y
        print(z)
        x = int(input('введите X = '))
        y = int(input('введите Y = '))
        sing = (input('введите знак = '))
    else:
        print('введите корректный знак')
        x = int(input('введите X = '))
        y = int(input('введите Y = '))
        sing = (input('введите знак = '))
else:
    print('конец')