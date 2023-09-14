def concats(seq, tims):
    return seq * tims


def counts(seq, part):
    counter = 0
    for x in seq:
        if x == part:
            counter += 1
    return counter


def reverse(seq):
    return seq[::-1]


def first_last(seq):
    return seq[0], seq[-1]


def has_two_X(seq):
    counter = 0
    for x in seq:
        if x == "X":
            counter += 1
    return counter == 2


def has_duplicates(seq):
    seen = set()
    for x in seq:
        if x in seen:
            return True
        seen.add(x)
    return False
