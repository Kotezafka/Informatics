def number_of_even_elements():
    i = 0
    n = int(input())
    if n == 0:
        return 0
    while n != 0:
        if n % 2 == 0:
            i += 1
        n = int(input())
    return i


a = number_of_even_elements()
print(a)
