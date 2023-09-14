def inc(n):
    return (n+1)


def inc_with(n, t):
    return (n+t)


def dec(n):
    return (n-1)


def dec_with(n, t):
    return (n-t)


def greatest(n1, n2):
    if n1 >= n2:
        return n1
    else:
        return n2


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def power(x, n):
    return (x**n)


def factorial(n):
    ans = 1
    if n == 1:
        return (ans)
    else:
        return n * factorial(n-1)


def is_prime(tal):
    if tal < 2:
        return False
    for x in range(2, int(tal**0.5) + 1):
        if tal % x == 0:
            return False
    return True


# Test the code
print('41 plus 1:', inc(41))
print('30 plus 12:', inc_with(30, 12))

print('43 minus 1:', dec(43))
print('52 minus 10:', dec_with(52, 10))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 16:', power(2, 16))

print('Factorial of 5:', factorial(5))

print(is_prime(7))
