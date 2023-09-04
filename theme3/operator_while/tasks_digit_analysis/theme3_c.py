class Number:
    def __init__(self, n):
        self.n = n

    def min_and_max_numbers(self):
        n = self.n
        a = n % 10
        max = a
        min = a
        while n > 0:
            a = n % 10
            if a >= max:
                max = a
            elif a < min:
                min = a
            n = n // 10
        print(min, max)


def calculate_min_and_max_numbers(n):
    num = Number(n)

    num.min_and_max_numbers()


n = int(input())

calculate_min_and_max_numbers(n)
