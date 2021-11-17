from datetime import datetime, timedelta
trains=[
    {'number_train':234,'point_start':'Minsk','time_start':'11/6/21 15:02:34','point_stop':'Gomel','time_stop':'11/7/21 1:02:34'},
    {'number_train':623,'point_start':'vitebsk','time_start':'11/7/21 19:02:34','point_stop':'Grodno','time_stop':'11/8/21 16:10:34'},
    {'number_train':516,'point_start':'Riga','time_start':'11/9/21 3:02:34','point_stop':'Minsk','time_stop':'11/9/21 8:14:34'},
    {'number_train':54,'point_start':'Brest','time_start':'11/8/21 00:02:34','point_stop':'Lida','time_stop':'11/8/21 7:15:34'}
    ]

time_in_traver= timedelta(hours=7,minutes=20)
for i in trains:
    time_i=(i.get('time_start'))
    time_start=datetime.strptime(time_i,'%m/%d/%y %H:%M:%S')
    time_j = (i.get('time_stop'))
    time_stop = datetime.strptime(time_j, '%m/%d/%y %H:%M:%S')
    hour=time_stop-time_start
    if hour>=time_in_traver:
        print(f'время в пути {hour},{i}')
print(time_in_traver)