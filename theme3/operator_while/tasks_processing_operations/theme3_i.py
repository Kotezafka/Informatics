def number_of_max_elements():
    n = int(input())
    max = n
    i = 1
    if n == 0:
        return 0
    while n != 0:
        n = int(input())
        if n > max:
            i = 0
            max = n
            i += 1
        elif n == max:
            i += 1
    return i


a = number_of_max_elements()
print(a)
