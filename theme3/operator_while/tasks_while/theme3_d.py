class Number:
    def __init__(self, n):
        self.n = n

    def powers_two(self):
        i = 1
        t = 0
        while i <= self.n:
            if i == self.n:
                t += 1
                print('YES')
                break
            i *= 2
        if t == 0:
            print('NO')


def calculate_powers_two(n):
    num = Number(n)

    num.powers_two()


n = int(input())

calculate_powers_two(n)
