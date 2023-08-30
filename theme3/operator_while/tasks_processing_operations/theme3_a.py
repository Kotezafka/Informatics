def sequence_length():
    i = 0
    n = int(input())
    if n == 0:
        return 0
    while n != 0:
        i += 1
        n = int(input())
    return i


a = sequence_length()
print(a)
