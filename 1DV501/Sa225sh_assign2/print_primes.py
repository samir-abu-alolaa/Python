import time


def is_prime(tal):
    if tal < 2:
        return False
    for x in range(2, int(tal**0.5) + 1):
        if tal % x == 0:
            return False
    return True


def print_primes():
    n = int(input("How many primes? "))
    start_time = time.time()
    antal = 0
    ans = ""
    x = 2  # Start checking from 2

    while antal < n:
        if is_prime(x):
            antal += 1
            ans += " " + str(x)
            if antal % 10 == 0:
                ans += "\n"
        x += 1  # Move to the next number
    print(ans)
    print(time.time() - start_time)


print_primes()
