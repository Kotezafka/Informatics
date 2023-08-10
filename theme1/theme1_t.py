class Number:
    def __init__(self, number):
        self.number = number

    def symmetrical_number(self):
        fourth_digit = self.number % 10
        integer_division1 = self.number // 10

        third_digit = integer_division1 % 10
        integer_division2 = integer_division1 // 10

        second_digit = integer_division2 % 10
        integer_division3 = integer_division2 // 10

        first_digit = integer_division3 % 10

        return (((fourth_digit == first_digit) * 1 + (third_digit == second_digit) * 1) == 2) * 1


def calculate_symmetrical_number(number):
    num = Number(number)

    a = num.symmetrical_number()
    print(a)


number = int(input())

calculate_symmetrical_number(number)
