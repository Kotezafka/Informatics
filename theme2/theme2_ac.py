class Number:
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def even_number(self):
        if (self.number1 % 2 == 0 and self.number2 % 2 == 0 and self.number3 % 2 == 0) or (self.number1 % 2 != 0 and self.number2 % 2 != 0 and self.number3 % 2 != 0):
            print('NO')
        else:
            print('YES')


def calculate_even_number(number1, number2, number3):
    num = Number(number1, number2, number3)

    num.even_number()


number1 = int(input())
number2 = int(input())
number3 = int(input())

calculate_even_number(number1, number2, number3)
