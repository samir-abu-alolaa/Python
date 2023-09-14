import random


def creat_luck():
    lst = []
    while len(lst) <= 6:
        ran_num = random.randint(1, 35)
        if ran_num not in lst:
            lst.append(ran_num)
    print(sorted(lst))


creat_luck()
