class Number:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def remainder(self):
        for i in range(self.a, self.b + 1):
            if i % self.d == self.c:
                print(i, end = ' ')


def calculate_remainder(a, b, c, d):
    num = Number(a, b, c, d)

    num.remainder()


a = int(input())
b = int(input())
c = int(input())
d = int(input())

calculate_remainder(a, b, c, d)
