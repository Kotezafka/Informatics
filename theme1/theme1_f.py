class Number:
    def __init__(self, number):
        self.number = number

    def remainder_of_the_division(self):
        a = self.number % 10
        return a


def calculate_last_of_digit(number):
    num = Number(number)

    return num.remainder_of_the_division()
