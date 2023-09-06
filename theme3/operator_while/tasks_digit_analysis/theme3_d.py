class Number:
    def __init__(self, n):
        self.n = n

    def binary_notation_of_number(self):
        n = self.n
        s = str()
        if n == 0:
            return 0
        while n > 1:
            a = n % 2
            s += str(a)
            n = n // 2
        s += str(1)
        return s


def find_binary_notation_of_number(n):
    num = Number(n)

    return num.binary_notation_of_number()


n = int(input())

a = find_binary_notation_of_number(n)
print(a)
