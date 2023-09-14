from random import randint as rd


def two_dice():
    dice_valu = {
        2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
        7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0
    }

    for roll in range(10000):
        dice_res = rd(2, 12)
        dice_valu[dice_res] += 1
    for key, value in dice_valu.items():
        print(key, end="     ")
        print(value, end="\n")


two_dice()
