def amount_elements_bigger_than_previous():
    n = int(input())
    c = n
    i = 0
    if n == 0:
        return 0
    while n != 0:
        n = int(input())
        if n > c:
            i += 1
        c = n
    return i


a = amount_elements_bigger_than_previous()
print(a)
