class Number:
    def __init__(self, n):
        self.n = n

    def square_number(self):
        i = 1
        t = self.n ** 0.5
        while i <= t:
            print(i ** 2)
            i += 1


def calculate_square_number(n):
    num = Number(n)

    num.square_number()


n = int(input())

calculate_square_number(n)
