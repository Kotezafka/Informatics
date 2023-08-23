class Number:
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def sum_geometric_progression(self):
        sum = 1
        for i in range(1, self.n + 1):
            sum += self.a ** i
        print(sum)


def calculate_sum_geometric_progression(a, n):
    num = Number(a, n)

    num.sum_geometric_progression()


a = float(input())
n = int(input())

calculate_sum_geometric_progression(a, n)
