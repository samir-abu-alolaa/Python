import random

def odd_or_even():
    num = random.randint(-10, 10)
    if num > 0:
        if num % 2 == 0:
            print(f"The generated number is {num}\n{num} is even and positive")
        else:
            print(f"The generated number is {num}\n{num} is odd and positive")
    elif num < 0:
        if num % 2 == 0:
            print(f"The generated number is {num}\n{num} is even and negative")
        else:
            print(f"The generated number is {num}\n{num} is odd and negative")
    else:
        print(f"The generated number is {num}\n{num} is even and neither positive nor negative")

odd_or_even()
