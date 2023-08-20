class Equation:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def equation_roots(self):
        if self.a == 0:
            if self.b != 0:
                print('NO')
            else:
                if self.d == 0:
                    print('NO')
                else:
                    print('INF')
        else:
            x = - self.b / self.a
            if self.c * x + self.d == 0:
                print('NO')
            else:
                if self.b == 0:
                    print(x)
                if self.b != 0:
                    if x == int(x):
                        print(int(x))
                    else:
                        print('NO')


def calculate_equation_roots(a, b, c, d):
    num = Equation(a, b, c, d)

    num.equation_roots()


a = int(input())
b = int(input())
c = int(input())
d = int(input())

calculate_equation_roots(a, b, c, d)
