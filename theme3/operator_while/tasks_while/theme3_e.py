class Number:
    def __init__(self, n):
        self.n = n

    def binary_log(self):
        k = 0
        i = 1
        while i < self.n:
            i *= 2
            k += 1
        print(k)


def calculate_binary_log(n):
    num = Number(n)

    num.binary_log()


n = int(input())

calculate_binary_log(n)
