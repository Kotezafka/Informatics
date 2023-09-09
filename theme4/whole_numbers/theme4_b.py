class Number:
    def __init__(self, n):
        self.n = n

    def sum_from_1_to_n(self):
        s = 0
        if self.n >= 0:
            sum = ((1 + self.n) * self.n) / 2
            # for i in range(1, self.n + 1):
            #     s += i
        else:
            # for i in range(1, self.n - 1, -1):
            #     s += i
            sum = - (((1 + -self.n) * (-self.n)) / 2) + 1
        print(sum)


def calculate_sum_from_1_to_n(n):
    num = Number(n)

    num.sum_from_1_to_n()


n = int(input())

calculate_sum_from_1_to_n(n)
