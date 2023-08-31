def max_sequence():
    n = int(input())
    if n == 0:
        return 0
    max = n
    while n != 0:
        n = int(input())
        if n > max:
            max = n
    return max


a = max_sequence()
print(a)
