class Number:
    def __init__(self, n):
        self.n = n

    def is_palindromes(self, i):
        s = str()
        f = i
        while i > 0:
            a = i % 10
            s += str(a)
            i = i // 10
        if s == str(f):
            return 1
        return 0

    def number_of_palindromes(self):
        k = 0
        for i in range(1, self.n + 1):
            if self.is_palindromes(i):
                k += 1
        return k


def calculate_number_of_palindromes(n):
    num = Number(n)

    return num.number_of_palindromes()


n = int(input())

a = calculate_number_of_palindromes(n)
print(a)
