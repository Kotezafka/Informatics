class Number:
    def __init__(self, n):
        self.n = n

    def sum_of_powers(self):
        a = 1
        sum = 0
        for i in range(0, self.n + 1):
            sum += a
            a *= 2
        print(sum)


def calculate_sum_of_powers(n):
    num = Number(n)

    num.sum_of_powers()


n = int(input())

calculate_sum_of_powers(n)
