ent_str = str(input("Введите текст"))
fst_str = len(ent_str)
good_str = fst_str/2
if fst_str % 2 == 0:
    print(ent_str[int(good_str)-1:int(good_str)])
if fst_str % 2 != 0:
    print(ent_str[int(good_str)])
if (ent_str[int(good_str)]) == ent_str[0]:
        print(ent_str[1:-1])
else:
    pass
