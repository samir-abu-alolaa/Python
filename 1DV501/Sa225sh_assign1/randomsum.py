import random
def randomnum():
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)
    d = random.randint(1,100)
    e = random.randint(1,100)
    ans = a+ b+ c+ d+ e
    print(f"Five random numbers: {a} {b} {c} {d} {e}\n The sum is {ans} ")
randomnum()