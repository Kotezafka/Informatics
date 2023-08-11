class Number:
    def __init__(self, number):
        self.number = number

    def leap_year(self):
        if (self.number % 4 == 0 and self.number % 100 != 0) or self.number % 400 == 0:
            print('YES')
        else:
            print('NO')


def calculate_leap_year(number):
    num = Number(number)

    num.leap_year()


number = int(input())

calculate_leap_year(number)
