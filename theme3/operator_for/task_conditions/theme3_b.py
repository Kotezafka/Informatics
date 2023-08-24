class Number:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def remainder(self):
        for i in range(self.a + (self.c - (self.a % self.d)), self.b + 1, self.d):
            print(i, end=' ')


def calculate_remainder(a, b, c, d):
    num = Number(a, b, c, d)

    num.remainder()


a = int(input())
b = int(input())
c = int(input())
d = int(input())

calculate_remainder(a, b, c, d)
