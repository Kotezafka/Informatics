class Number:
    def __init__(self, n):
        self.n = n

    def sum_of_numbers(self):
        s = 0
        for i in range(1, self.n + 1):
            m = int(input())
            s += m
        return s


def calculate_sum_of_numbers(n):
    num = Number(n)

    return num.sum_of_numbers()


n = int(input())

x = calculate_sum_of_numbers(n)
print(x)
