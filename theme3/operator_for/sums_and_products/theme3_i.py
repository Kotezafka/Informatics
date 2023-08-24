class Number:
    def __init__(self, n):
        self.n = n

    def sum(self):
        sum = 1
        fact = 1
        for i in range(2, self.n + 2):
            sum += 1 / fact
            fact *= i
        print(sum)


def calculate_sum(n):
    num = Number(n)

    num.sum()


n = int(input())

calculate_sum(n)
