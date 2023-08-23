class Number:
    def __init__(self, n):
        self.n = n

    def factorial(self):
        factorial = 1
        for i in range(1, self.n + 1):
            factorial *= i
        print(factorial)


def calculate_factorial(n):
    num = Number(n)

    num.factorial()


n = int(input())

calculate_factorial(n)
