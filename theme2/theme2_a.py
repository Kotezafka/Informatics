class Number:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def largest_number(self):
        if self.number1 > self.number2:
            print(self.number1)
        else:
            print(self.number2)


def calculate_largest_number(number1, number2):
    num = Number(number1, number2)

    num.largest_number()


number1 = int(input())
number2 = int(input())

calculate_largest_number(number1, number2)
