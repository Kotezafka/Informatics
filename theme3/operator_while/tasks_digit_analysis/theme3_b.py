class Number:
    def __init__(self, n):
        self.n = n

    def amount_of_zeros(self):
        i = 0
        n = self.n
        while n > 0:
            a = n % 10
            if a == 0:
                i += 1
            n = n // 10
        print(i)


def calculate_amount_of_zeros(n):
    num = Number(n)

    num.amount_of_zeros()


n = int(input())

calculate_amount_of_zeros(n)
