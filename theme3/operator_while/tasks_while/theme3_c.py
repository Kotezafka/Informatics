class Number:
    def __init__(self, n):
        self.n = n

    def powers_of_two(self):
        i = 1
        while i <= self.n:
            print(i, end=' ')
            i *= 2


def calculate_powers_of_two(n):
    num = Number(n)

    num.powers_of_two()


n = int(input())

calculate_powers_of_two(n)
