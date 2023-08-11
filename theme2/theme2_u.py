class Number:
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def amount_of_equals_out_of_three(self):
        if self.number1 == self.number2 == self.number3:
            print(3)
        elif self.number1 == self.number2 or self.number2 == self.number3 or self.number1 == self.number3:
            print(2)
        else:
            print(0)


def calculate_amount_of_equals_out_of_three(number1, number2, number3):
    num = Number(number1, number2, number3)

    num.amount_of_equals_out_of_three()


number1 = int(input())
number2 = int(input())
number3 = int(input())

calculate_amount_of_equals_out_of_three(number1, number2, number3)
