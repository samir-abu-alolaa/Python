def shortname():
    first  = input("First name: ")
    middle = input("middle name: ")
    last   = input("last name: ")
    fir    = first[0]+"."+" "
    mid    = middle[0]+"."+" "
    las    = last[:4]
    print(f"Short name: {fir}{mid}{las}")
shortname()