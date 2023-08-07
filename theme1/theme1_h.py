class Number:
    def __init__(self, number):
        self.number = number

    def integer_division_and_remainder(self):
        number_after_integer_division = self.number // 10
        number_of_tens = number_after_integer_division % 10

        return number_of_tens


def calculate_the_number_of_tens(number):
    num = Number(number)

    return num.integer_division_and_remainder()
