def odd_using_for():
    input_n = int(input("Enter a positive integer: "))
    counter_while = -1
    print("for loop: ", end=" ")
    for x in range(1, input_n, 2):
        print(x, end=" ")
    print("\n", end="")
    print("while loop: ", end=" ")
    while counter_while < input_n-2:
        counter_while += 2
        print(counter_while, end=" ")


odd_using_for()
