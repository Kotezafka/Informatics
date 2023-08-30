class Number:
    def __init__(self, n):
        self.n = n

    def fibonacci_number(self):
        i = 1
        k0 = 0
        k1 = 1
        f = 0
        if self.n == 1:
            return k0 + k1

        while i < self.n:
            f = k0 + k1

            if i % 2 != 0:
                k0 = f
            else:
                k1 = f
            i += 1
        return f


def calculate_fibonacci_number(n):
    num = Number(n)

    a = num.fibonacci_number()
    print(a)


n = int(input())

calculate_fibonacci_number(n)