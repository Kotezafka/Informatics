class NeighboringNumbers:
    def __init__(self, number):
        self.number = number

    def calculate_next(self):
        a = self.number + 1
        return a

    def calculate_previous(self):
        b = self.number - 1
        return b


def line_output(number):
    a = NeighboringNumbers(number)

    print("The next number for the number ", a.number, " is ", a.calculate_next(), ". \nThe previous number for the number ", a.number, " is ", a.calculate_previous(), ".", sep='')


number = int(input())
line_output(number)
