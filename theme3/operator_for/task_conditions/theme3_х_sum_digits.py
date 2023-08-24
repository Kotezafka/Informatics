class Number:
    def __init__(self, x):
        self.x = x

    def sum_of_digits(self):
        s = 0
        while self.x != 0:
            remainder = self.x % 10
            s += remainder
            self.x = self.x // 10
        return s


def calculate_sum_of_digits(x):
    num = Number(x)

    return num.sum_of_digits()


x = int(input())

n = calculate_sum_of_digits(x)
print(n)
