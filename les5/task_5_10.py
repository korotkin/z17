from pprint import pprint

trains = [
    {
        'train': 514,
        'in': 'Витебск',
        'out': "Минск",
        'time in': "23:00",
        'time out': "4:30",
    },
    {
        'train': 41,
        'in': 'Санкт-Петербург',
        'out': "Прага",
        'time in': "4:15",
        'time out': "18:40",
    },
    {
        'train': 777,
        'in': 'Вильнюс',
        'out': "Москва",
        'time in': "05:00",
        'time out': "22:00",
    },
    {
        'train': 59,
        'in': 'Киев',
        'out': "Брест",
        'time in': "18:52",
        'time out': "06:18",
    },
]
new_dict = {}
time_dict = {}
time_in_sec = []
time_out_sec = []
list_of_trains = []
j = 0


for i in trains:
    for key, value in i.items():
        if key == 'time in':
            time = i.get(key, 0)
            time_list = time.split(':')
            sec = int(time_list[0]) * 60 + int(time_list[1])
            time_in_sec.append(sec)
        elif key == 'time out':
            time = i.get(key, 0)
            time_list = time.split(':')
            sec = int(time_list[0]) * 60 + int(time_list[1])
            time_out_sec.append(sec)
            while j != len(time_out_sec):
                if time_out_sec[j] > time_in_sec[j]:
                    z = 1440 - (time_out_sec[j] - time_in_sec[j])
                    if z > 440:
                        train = i.get("train", 0)
                        list_of_trains.append(train)
                        j += 1
                    else:
                        j += 1
                elif time_out_sec[j] < time_in_sec[j]:
                    z = time_in_sec[j] - time_out_sec[j]
                    if z > 440:
                        train = i.get("train", 0)
                        list_of_trains.append(train)
                        j += 1
                    else:
                        j += 1
    for n in list_of_trains:
        if n == i.get('train', 0):
            pprint(i)


