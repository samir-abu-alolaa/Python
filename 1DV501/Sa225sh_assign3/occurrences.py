import random


def create_random():
    seq = []
    i = 0
    while i < 100: 
        i += 1
        n = random.randint(1, 10)
        seq.append(n)
    return count_occurrences(seq)


def count_occurrences(seq):
    seq = sorted(seq)
    ans = {}
    for key in seq:
        if key not in ans:
            ans[key] = 1
        else:
            ans[key] += 1
    for key, value in ans.items():  
        print(key, "  ", value)


create_random()
