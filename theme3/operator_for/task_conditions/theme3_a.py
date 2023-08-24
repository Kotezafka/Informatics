class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def even_numbers(self):
        for i in range(self.a + self.a % 2, self.b + 1, 2):
            print(i, end=' ')


def find_even_numbers(a, b):
    num = Number(a, b)

    num.even_numbers()


a = int(input())
b = int(input())

find_even_numbers(a, b)
