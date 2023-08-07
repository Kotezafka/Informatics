class Number:
    def __init__(self, number):
        self.number = number

    def integer_division(self):
        a = self.number // 10
        return a


def calculate_the_number_of_tens(number):
    num = Number(number)

    return num.integer_division()


number = int(input())

a = calculate_the_number_of_tens(number)
print(a)
