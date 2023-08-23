class Number:
    def __init__(self, n):
        self.n = n

    def sum(self):
        sum = 0
        for i in range(0, self.n + 1):
            sum += ((-1) ** i) / ((2 * i) + 1)
            sum1 = 4 * sum
        print(sum1)


def calculate_sum(n):
    num = Number(n)

    num.sum()


n = int(input())

calculate_sum(n)
