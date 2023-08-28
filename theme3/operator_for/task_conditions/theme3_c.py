class NUmber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def full_square(self):
        for i in range(self.a, self.b + 1):
            for g in range(0, int(i**0.5) + 1):
                if i != int(g) * int(g):
                    g += 1
                elif i == int(g) * int(g):
                    print(i, end=' ')


def calculate_full_square(a, b):
    num = NUmber(a, b)

    num.full_square()


a = int(input())
b = int(input())

calculate_full_square(a, b)
