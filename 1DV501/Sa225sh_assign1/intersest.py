def intrest():
    savings = int(input("Initial savings: "))
    p = float(input("Interest rate: "))
    years = int(input("Number of years: "))

    multiplication_factor = (p / 100) + 1
    ans = savings * (multiplication_factor ** years)

    print(round(ans))

intrest()
