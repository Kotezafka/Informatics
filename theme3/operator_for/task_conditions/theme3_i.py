class Number:
    def __init__(self, x):
        self.x = x

    def number_of_divisors(self):
        if self.x == 1:
            print(1)
        else:
            amount = 1
            i = 0
            for i in range(2, int((self.x ** 0.5) + 1)):
                if self.x % i == 0:
                    amount += 2
            if i ** 2 == self.x:
                print(amount)
            else:
                print(amount + 1)


def calculate_number_of_divisors(x):
    num = Number(x)

    num.number_of_divisors()


x = int(input())

calculate_number_of_divisors(x)
