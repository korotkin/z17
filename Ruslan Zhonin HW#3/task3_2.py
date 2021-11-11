#task2
guests_num = input('Number of guests=')
if int(guests_num) > 50:
    print('restaurant')
elif 20 <= int(guests_num) <= 50:
    print('cafe')
else:
    print('home')
