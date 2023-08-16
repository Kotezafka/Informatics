class Quadratic_equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def equation_roots(self):
        if self.b != 0:
            if self.c != 0:
                discriminant = self.b ** 2 - 4 * self.a * self.c
                if discriminant > 0:
                    x1 = (- self.b + discriminant ** 0.5) / (2 * self.a)
                    x2 = (- self.b - discriminant ** 0.5) / (2 * self.a)
                    print(x1, x2)
                if discriminant == 0:
                    x1 = - self.b / (2 * self.a)
                    print(x1)
            else:
                x1 = 0
                x2 = - self.b / self.a
                print(x1, x2)
        else:
            if self.c < 0:
                x1 = (self.c / self.a) ** 0.5
                x2 = - (self.c / self.a) ** 0.5
                print(x1, x2)
            if self.c == 0:
                print(0)


def calculate_equation_roots(a, b, c):
    num = Quadratic_equation(a, b, c)

    num.equation_roots()


a = float(input())
b = float(input())
c = float(input())

calculate_equation_roots(a, b, c)
