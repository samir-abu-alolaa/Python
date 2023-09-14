import random


def gen():
    inp = int(input("Enter number of integers to be generated: "))

    if inp <= 0:
        print("Error: The input must be a positive integer.")
        return

    min_value = 101
    max_value = 0
    sum_values = 0

    generated_values = []

    for x in range(inp):
        num = random.randint(1, 100)
        generated_values.append(num)

        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
        sum_values += num

    average = sum_values / inp

    print(f"Generated values: {' '.join(map(str, generated_values))}")
    print(f"Average, min, and max are {average:.2f},\
{min_value}, and {max_value}")


gen()
