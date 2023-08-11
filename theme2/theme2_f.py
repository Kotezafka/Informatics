class Number:
    def __init__(self, number1, number2, number3):
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
        self.max = self.number1

    def maximum_of_three(self):

        if self.max < self.number2:
            self.max = self.number2

        if self.max < self.number3:
            self.max = self.number3

        print(self.max)


def calculate_maximum_of_three(number1, number2, number3):
    num = Number(number1, number2, number3)

    num.maximum_of_three()


number1 = int(input())
number2 = int(input())
number3 = int(input())

calculate_maximum_of_three(number1, number2, number3)