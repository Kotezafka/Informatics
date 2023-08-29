class Athlete:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def day_number(self):
        day = 1
        k = self.x
        while k < self.y:
            k += k * 0.1
            day += 1
        print(day)


def calculate_day_number(x, y):
    num = Athlete(x, y)

    num.day_number()


x = int(input())
y = int(input())

calculate_day_number(x, y)
