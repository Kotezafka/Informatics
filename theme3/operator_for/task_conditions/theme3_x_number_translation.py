class Number:
    def __init__(self, n):
        self.n = n

    def decimal_system(self):
        t = self.n
        d = 0
        sum1 = 0
        while t >= 1:
            remainder = t % 10
            t = t // 10

            sum1 += remainder * 2**d
            d += 1
        print(sum1)


def calculate_decimal_system(n):
    num = Number(n)

    num.decimal_system()


n = int(input())

calculate_decimal_system(n)
