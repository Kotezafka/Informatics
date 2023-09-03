def second_numbers():
    n = int(input())
    max1 = n
    max2 = 0
    if n == 0:
        return 0
    while n != 0:
        n = int(input())
        if n >= max1:
            max2 = max1
            max1 = n
        elif n >= max2 and n < max1:
            max2 = n
    return max2


a = second_numbers()
print(a)
