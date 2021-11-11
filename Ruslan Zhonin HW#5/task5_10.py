# ) Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах,
# время пребывания в пути которых превышает 7 часов 20 минут.[02-7.3-ML02]
# Примечание: данное задание подразумевает самостоятельное изучение принципов работы со
# временем в Python(библиотека datetime)

import datetime

trains_list = {123:{'Minsk': datetime.time(9, 10), 'Grodno': datetime.time(18, 20)},
               456:{'Vitebsk': datetime.time(12, 30), 'Orsha': datetime.time(14, 00)},
               889:{'Gomel': datetime.time(8, 30), 'Minsk': datetime.time(22, 40)},
               464:{'Moskow': datetime.time(23, 30), 'Kiev': datetime.time(18, 40)}}

for key in trains_list:
    train_props = trains_list[key]
    times = []
    for item in train_props:
        time = train_props[item]
        times.append(time)
    arrival_time = datetime.datetime.combine(datetime.date.today(), times[0])
    recieve_time = datetime.datetime.combine(datetime.date.today(), times[1])
    time_delta = recieve_time - arrival_time
    if time_delta.total_seconds() / 3600 > 7.20:
        print(f"{key}: {train_props}")