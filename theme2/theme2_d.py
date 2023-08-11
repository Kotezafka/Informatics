class Number:
    def __init__(self, number):
        self.number = number

    def number_sign(self):
        if self.number > 0:
            print('1')
        elif self.number < 0:
            print('-1')
        else:
            print('0')


def calculate_number_sign(number):
    num = Number(number)

    num.number_sign()


number = int(input())

calculate_number_sign(number)
