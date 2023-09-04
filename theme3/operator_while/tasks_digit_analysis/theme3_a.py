class Number:
    def __init__(self, n):
        self.n = n

    def sum_digits_of_number(self):
        sum = 0
        n = self.n
        while n > 0:
            a = n % 10
            sum += a
            n = n // 10
        print(sum)


def calculate_sum_digits_of_number(n):
    num = Number(n)

    num.sum_digits_of_number()


n = int(input())

calculate_sum_digits_of_number(n)
