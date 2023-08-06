from math import sqrt


class Gipotenuza:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def calculate_gipotenuza(self):
        c = sqrt(self.side1**2 + self.side2**2)
        return c


def calc_gipot(side1, side2):
    gipot = Gipotenuza(side1, side2)

    return gipot.calculate_gipotenuza()


side1 = int(input())
side2 = int(input())

g = calc_gipot(side1, side2)
print(g)
