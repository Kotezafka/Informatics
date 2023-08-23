class Number:
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def degree(self):
        deg = 0
        for i in range(0, self.n + 1):
            deg = self.a ** i
        print(deg)


def calculate_degree(a, n):
    num = Number(a, n)

    num.degree()


a = float(input())
n = int(input())

calculate_degree(a, n)
