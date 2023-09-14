def conv_to_C():
    f = float(input("Provide a temperature in Fahrenheit: "))
    c = (5/9) * (f - 32)
    print(round(c,2))
conv_to_C()