def classifay():
    target = int(input("Please provide an integer: "))
    if target < 0:
        print(f"{target} is negative")
    elif target > 0: 
        print(f"{target} is positive")
    else: 
        print(f"{target} is Zero")
classifay()