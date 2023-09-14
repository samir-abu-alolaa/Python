def print_tr():
    n = int(input("Provide an odd positve number: "))
    tri = "*"
    cont = 0
    space = " "
    for x in range(n, 0, -1):
        ans = space*cont+tri * x
        cont += 1

        print(ans)
    print("\nIsosceles Triangle:")
    for i in range(n, 0, -2):
        spaces = " " * ((n - i) // 2)
        stars = "*" * i
        print(spaces + stars)


print_tr()
