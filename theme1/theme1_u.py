class Number:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def divisibility_check(self):
        return (((self.number1 % self.number2 == 0) * 1 + (self.number2 % self.number1 == 0) * 1) != 0) * 1


def calculate_divisibility_check(number1, number2):
    num = Number(number1, number2)

    a = num.divisibility_check()
    print(a)


number1 = int(input())
number2 = int(input())

calculate_divisibility_check(number1, number2)
