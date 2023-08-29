class Number:
    def __init__(self, x, p, y):
        self.x = x
        self.p = p
        self.y = y

    def number_of_years(self):
        year = 0
        sum = self.x
        while sum < self.y:
            sum += sum * (self.p * 0.01)
            if sum % 1 != 0:
                sum = sum // 1
            year += 1
        print(year)


def calculate_number_of_years(x, p, y):
    num = Number(x, p, y)

    num.number_of_years()


x = int(input())
p = int(input())
y = int(input())

calculate_number_of_years(x, p, y)
