class Number:
    def __init__(self, n):
        self.n = n

    def counting_numbers(self):
        zero = 0
        positive_numbers = 0
        negative_numbers = 0

        for i in range(1, self.n + 1):
            m = int(input())
            if m == 0:
                zero += 1

            if m > 0:
                positive_numbers += 1

            if m < 0:
                negative_numbers += 1

        print(zero, positive_numbers, negative_numbers)


def calculate_counting_numbers(n):
    num = Number(n)

    num.counting_numbers()


n = int(input())

calculate_counting_numbers(n)

