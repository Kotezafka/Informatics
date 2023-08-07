class Number:
    def __init__(self, number):
        self.number = number

    def integer_division_and_remainder(self):
        number_of_units = self.number % 10

        number_after_integer_division = self.number // 10
        number_of_tens = number_after_integer_division % 10

        number_of_hundreds = self.number // 100

        sum_of_three_digits = number_of_units + number_of_tens + number_of_hundreds

        return sum_of_three_digits


def calculate_sum_of_a_three_digit_number(number):
    num = Number(number)

    return num.integer_division_and_remainder()


number = int(input())

sum_of_three_digits = calculate_sum_of_a_three_digit_number(number)
print(sum_of_three_digits)
