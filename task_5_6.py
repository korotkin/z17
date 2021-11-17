massive=[1, 2, 5, 1,4, 8, 9]
kolvo=0
print(massive)
for i in range(len(massive)-1):
    if massive[i+1]-massive[i]==1:
        print(i)
        if i + 2 == len(massive):
            kolvo += 1
        elif massive[i+2]-massive[i+1]!=1:
            kolvo+=1
print(f'монотонных возрастаний {kolvo}')