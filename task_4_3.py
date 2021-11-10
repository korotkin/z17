d_ary = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for key in list(d_ary.keys()):
    d_ary[key + str(len(key))] = d_ary.pop(key)
print(d_ary)
