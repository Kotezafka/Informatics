def average_value_sequence():
    sum = 0
    i = 0
    n = int(input())
    if n == 0:
        return 0
    while n != 0:
        sum += n
        n = int(input())
        i += 1
    average_value = sum / i
    return average_value


a = average_value_sequence()
print(a)
