def sequence_sum():
    sum = 0
    n = int(input())
    if n == 0:
        return 0
    while n != 0:
        sum += n
        n = int(input())
    return sum


a = sequence_sum()
print(a)
