def creat_list():
    ans = []
    state = True
    while state:
        inpu = int(input("Enter positive integers.\
End by giving a negative integer: "))
        if inpu < 0:
            state = False
            return ans
        else:
            ans.append(inpu)


print(creat_list())
