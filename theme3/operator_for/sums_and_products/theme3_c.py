class Number:
    def __init__(self, n):
        self.n = n

    def degree_of(self):
        expression = 1
        for i in range(1, self.n + 1):
            expression = 2 ** i
        print(expression)


def calculate_degree_of(n):
    num = Number(n)

    num.degree_of()


n = int(input())

calculate_degree_of(n)
