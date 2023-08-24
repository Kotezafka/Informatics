class Number:
    def __init__(self, n):
        self.n = n

    def zero(self):
        z = 0
        for i in range(1, self.n + 1):
            m = int(input())
            if m == 0:
                z += 1
        if z == 0:
            print('NO')
        else:
            print('YES')


def calculate_zero(n):
    num = Number(n)

    num.zero()


n = int(input())

calculate_zero(n)
