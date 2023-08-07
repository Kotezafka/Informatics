class Number:
    def __init__(self, number):
        self.number = number

    def remainder_of_the_division(self):
        a = self.number % 10
        return a


def last_digit(number):
    numb = Number(number)

    return numb.remainder_of_the_division()


number = int(input())

a = last_digit(number)
print(a)
