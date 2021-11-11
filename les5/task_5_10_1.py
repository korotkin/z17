from pprint import pprint

from datetime import datetime, timedelta

trains = [
    {'train': 234,
     'from': 'Санкт-Петербург',
     'time_form': '11/6/21 15:02',
     'to': 'Гомель',
     'time_to': '11/7/21 1:02'},
    {'train': 623,
     'from': 'Витебск',
     'time_form': '11/7/21 19:02',
     'to': 'Прага',
     'time_to': '11/8/21 16:10'},
    {'train': 516,
     'from': 'Варшава',
     'time_form': '11/9/21 3:02',
     'to': 'Москва',
     'time_to': '11/9/21 8:14'},
    {'train': 54,
     'from': 'Брест',
     'time_form': '11/8/21 00:02',
     'to': 'Бухарест',
     'time_to': '11/8/21 7:15'}
]

time_max = timedelta(hours=7, minutes=20)
for i in trains:
    time_form = i.get('time_form')
    time_form = datetime.strptime(time_form, '%m/%d/%y %H:%M')
    time_to = i.get('time_to')
    time_to = datetime.strptime(time_to, '%m/%d/%y %H:%M')
    time_in_road = time_to - time_form
    if time_in_road >= time_max:
        pprint(i)
