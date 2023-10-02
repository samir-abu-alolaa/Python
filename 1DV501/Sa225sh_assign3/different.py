import random


def creat_random():
    seq = []
    i = 0
    while i < 100:
        i += 1
        n = random.randint(1, 200)
        seq.append(n)
    return different(seq)


def different(seq):
    seq = sorted(seq)
    uniqe = []
    for x in seq:
        if x not in uniqe:
            uniqe.append(x)
    print(f"Different integers:\n{uniqe}")


creat_random()
