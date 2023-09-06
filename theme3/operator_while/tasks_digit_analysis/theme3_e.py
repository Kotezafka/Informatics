class Number:
    def __init__(self, n):
        self.n = n

    def number_inversion(self):
        n = self.n
        s = str()
        if n == 0:
            return 0
        while n > 0:
            a = n % 10
            s += str(a)
            n = n // 10
        return s


def calculate_number_inversion(n):
    num = Number(n)

    return num.number_inversion()


n = int(input())

a = calculate_number_inversion(n)
print(a)
