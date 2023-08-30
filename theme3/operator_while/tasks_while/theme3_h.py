class Number:
    def __init__(self, n):
        self.n = n

    def fibonacci_number(self):
        i = 1
        f0 = 0
        f1 = 1
        f = 0
        if self.n == 1:
            return f0 + f1

        while i < self.n:
            f = f0 + f1

            if i % 2 != 0:
                f0 = f
            else:
                f1 = f
            i += 1
        return f


def calculate_fibonacci_number(n):
    num = Number(n)

    a = num.fibonacci_number()
    print(a)


n = int(input())

calculate_fibonacci_number(n)
