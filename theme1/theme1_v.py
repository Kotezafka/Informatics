class Number:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def largest_number(self):
        return (self.number1 >= self.number2) * self.number1 + (self.number1 < self.number2) * self.number2


def calculate_largest_number(number1, number2):
    num = Number(number1, number2)

    a = num.largest_number()
    print(a)


number1 = int(input())
number2 = int(input())

calculate_largest_number(number1, number2)