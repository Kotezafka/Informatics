class Number:
    def __init__(self, x, p, y):
        self.x = x
        self.p = p
        self.y = y

    def number_of_years(self):
        self.x = self.x * 100
        self.y = self.y * 100
        self.p = self.p + 100
        year = 0
        while self.x < self.y:
            self.x = (self.x * self.p) // 100
            year += 1
        print(year)


def calculate_number_of_years(x, p, y):
    num = Number(x, p, y)

    num.number_of_years()


x = int(input())
p = int(input())
y = int(input())

calculate_number_of_years(x, p, y)
