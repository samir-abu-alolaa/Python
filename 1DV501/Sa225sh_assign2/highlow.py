import random


def gusse():
    counter = 0
    random_num = random.randint(1, 100)
    guss_input = int(input("Provide your gusse: "))
    while guss_input != random_num:
        counter += 1
        if guss_input < random_num:
            print("Clue: Higher")
            guss_input = int(input("Provide your gusse: "))

        else:
            print("Clue: Lower")
            guss_input = int(input("Provide your gusse: "))

    print(f"Correct answer after only {counter} guesses - Excellent!")


gusse()
