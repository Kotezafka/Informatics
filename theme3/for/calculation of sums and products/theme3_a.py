class Number:
    def __init__(self, n):
        self.n = n

    def sum(self):
        sum = 0
        for i in range(1, self.n + 1):
            sum += i ** 2
        print(sum)


def calculate_sum(n):
    num = Number(n)

    num.sum()


n = int(input())

calculate_sum(n)
