class Number:
    def __init__(self, x):
        self.x = x

    def min_divisor(self):
        i = 2
        while self.x % i != 0:
            i += 1
        return i


def calculate_min_divisor(x):
    num = Number(x)

    return num.min_divisor()


x = int(input())

n = calculate_min_divisor(x)
print(n)
