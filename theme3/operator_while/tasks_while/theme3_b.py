class Number:
    def __init__(self, n):
        self.n = n

    def min_divisor(self):
        i = 2
        while i <= self.n:
            if self.n % i == 0:
                print(i)
                break
            i += 1


def calculate_min_divisor(n):
    num = Number(n)

    num.min_divisor()


n = int(input())

calculate_min_divisor(n)
