class Number:
    def __init__(self, n):
        self.n = n

    def degree(self):
        expression = 1
        for i in range(1, self.n + 1):
            expression = 2**i
        print(expression)


def calculate_degree(n):
    num = Number(n)

    num.degree()


n = int(input())

calculate_degree(n)
