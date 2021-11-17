zone_start = 200
zone_stop = 230
sum_delitel=0
dict={}
h={}
for elem in range(zone_start,zone_stop+1):
    range=2
    delitels=[]
    while range!=elem:
        if elem%range==0:
            delitels.append(range)
        range+=1
    dict.update({elem:delitels})
for i,k in dict.items():
    print(i,k)