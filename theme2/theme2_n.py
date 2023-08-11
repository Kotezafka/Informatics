class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def equation_roots(self):
        if self.a == 0 and self.b != 0:
            print('NO')

        if self.a == 0 and self.b == 0:
            print('INF')

        if self.a != 0 and self.b != 0 or self.a != 0 and self.b == 0:
            x = (- self.b) % self.a
            if x == 0:
                print((- self.b) // self.a)
            else:
                print('NO')


def calculate_equation_roots(a, b):
    num = Equation(a, b)

    num.equation_roots()


a = int(input())
b = int(input())

calculate_equation_roots(a, b)
