def sum_all():

    start_value = 0

    for num in range(1, 101):
        if num % 2 == 0:
            start_value += num
    print(f"Sum of the 100 first numbers is: {start_value}")


sum_all()
