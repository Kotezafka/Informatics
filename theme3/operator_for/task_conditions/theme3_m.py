class Number:
    def __init__(self, n):
        self.n = n

    def number_of_zeros(self):
        z = 0
        for i in range(1, self.n + 1):
            m = int(input())
            if m == 0:
                z += 1
        return z


def calculate_number_of_zeros(n):
    num = Number(n)

    return num.number_of_zeros()


n = int(input())

x = calculate_number_of_zeros(n)
print(x)
