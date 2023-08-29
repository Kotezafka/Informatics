class Number:
    def __init__(self, n):
        self.n = n

    def square_number(self):
        t = 1
        while t <= self.n:
            for i in range(1, int(t**0.5) + 1):
                if t != int(i) * int(i):
                    t += 1
                elif t == int(i) * int(i):
                    print(t, end=' ')


def calculate_square_number(n):
    num = Number(n)

    num.square_number()


n = int(input())

calculate_square_number(n)
