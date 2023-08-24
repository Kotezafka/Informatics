class Number:
    def __init__(self, x):
        self.x = x

    def number_divisors(self):
        for i in range(1, self.x + 1):
            if self.x % i == 0:
                print(i, end=' ')
            i += 1


def calculate_number_divisors(x):
    num = Number(x)

    num.number_divisors()


x = int(input())

calculate_number_divisors(x)
