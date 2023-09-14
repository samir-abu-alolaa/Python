import random


def random_num_list(n):
    lst = []
    for y in range(n):
        x = random.randint(1, 100)
        lst.append(x)
    return lst


def average(lst):
    sum = 0
    lenght = len(lst)
    for x in lst:
        sum += x
    print(round(sum/lenght))
    print(lst)


def only_odd(seq):
    ans = []
    for x in seq:
        if x % 2 != 0:
            ans.append(x)
    return ans


def to_string(lst):
    print(f'"{lst}"')


def contains(lst, a, b):
    n = 0
    for x in lst:
        n += 1
        if a in lst:
            if b == lst[n+1]:
                return True
            else:
                return False
        else:
            return False


def square(seq):
    n = [x**2 for x in seq]
    return n


def sublist(seq, start, end):
    ans = []
    for s in seq:
        if start <= s <= end:
            ans.append(s)
    return ans

# ___________________________________________________


print(contains([1, 2, 3, 4], 2, 3))
print(sublist([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(square([1, 2, 3, 4]))
print(random_num_list(7))
average(random_num_list(5))
print(only_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(to_string([1, 4, 5]))
