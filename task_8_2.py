"""
создать функцию проверки палиндрома слов
"""

def is_palindrom (*args):
    """
    :param args: str
    :return: palindroms
    """
    str_agrs=' '.join(args)
    massive=str_agrs.split(' ')
    massive_reverse=[i[::-1] for i  in massive]
    palindroms=str()
    for i in massive:
        for j in massive_reverse:
            if i==j:
                palindroms+=i
                palindroms+=' '
    return palindroms

print(is_palindrom('казак дед шалаш'))
print(is_palindrom('заказ тут летел кабак'))
print(is_palindrom('заказ есть летел нет'))
print(is_palindrom('есть два стула'))
