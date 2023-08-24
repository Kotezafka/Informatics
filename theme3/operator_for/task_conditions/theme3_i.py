class Number:
    def __init__(self, x):
        self.x = x

    def number_of_divisors(self):
        amount = 0
        for i in range(1, self.x + 1):
            if self.x % i == 0:
                amount += 1
        print(amount)


def calculate_number_of_divisors(x):
    num = Number(x)

    num.number_of_divisors()


x = int(input())

calculate_number_of_divisors(x)
