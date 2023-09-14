def find_k():
    n = int(input("Enter a positive integer: "))

    if n <= 0:
        print("Error: Please enter a positive integer")
        return

    sum_odd = 0
    sum_even = 0
    smallest_k = None
    largest_k = None

    for k in range(1, n + 1):
        if k % 2 == 1:  # Odd numbers
            sum_odd += k
            if sum_odd > n and smallest_k is None:
                smallest_k = k
        else:  # Even numbers
            sum_even += k
            if sum_even >= n and largest_k is None:
                largest_k = k

    if smallest_k is not None:
        print(f"{smallest_k} is the smallest k such that 1+3+5+...+k > {n}")
    else:
        print(f"No smallest k found for {n}")

    if largest_k is not None:
        print(f"{largest_k - 2 } is the largest k\
such that 0+2+4+6+...+k < {n}")
    else:
        print(f"No largest k found for {n}")


find_k()
