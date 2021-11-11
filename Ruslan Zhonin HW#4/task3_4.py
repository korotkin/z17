#task4
str = input('enter the string: ')
str_mid_symbol_index = len(str) // 2
if len(str)%2 == 0:
    print('string had an even symbol number')
else:
    if str[str_mid_symbol_index] == str[0]:
        print(str[0:str_mid_symbol_index])
    else:
        print('symbols are not identical')


