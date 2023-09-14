def is_palindrome(s):
    s = s.lower()
    pre_revers = ""
    after_revers = ""
    for elem in s:
        if elem.isalpha():
            after_revers += elem
            pre_revers += elem
    after_revers = after_revers[::-1]
    return after_revers == pre_revers


print(is_palindrome("Ni tal ar bra latin!"))
print(is_palindrome("A n ut for  as jar of tuna."))
print(is_palindrome("Was it a ra t I saw?"))
