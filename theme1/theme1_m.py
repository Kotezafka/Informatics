class Number:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def value_exchange(self):
        number3 = self.number1
        self.number1 = self.number2
        self.number2 = number3

        print(self.number1, self.number2)


def calculate_value_exchange(number1, number2):
    num = Number(number1, number2)

    num.value_exchange()


number1 = int(input())
number2 = int(input())

calculate_value_exchange(number1, number2)
