import tracemalloc
tracemalloc.start()

zone_start = 1
zone_stop = 50
for elem in range(zone_start,zone_stop+1):
    schet=1
    sum_delitel=0
    while schet!=elem:
        if elem%schet==0:
            sum_delitel+=schet
        schet+=1
    if sum_delitel>zone_start and sum_delitel<zone_stop:
        sum_delitel_delitel=0
        for j in range(1,sum_delitel):
            if sum_delitel%j==0:
                sum_delitel_delitel+=j
        if sum_delitel_delitel==elem:
            print(elem,sum_delitel)

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage is {current / 10**3}KB; Peak was {peak / 10**3}KB; Diff = {(peak - current) / 10**3}KB")
tracemalloc.stop()