class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def triangle_exist(self):
        if self.a >= self.b + self.c or self.b >= self.a + self.c or self.c >= self.a + self.b:
            print('impossible')
        else:
            if self.a > self.b and self.a > self.c:
                if self.b ** 2 + self.c ** 2 == self.a ** 2:
                    print('right')
                if self.b ** 2 + self.c ** 2 > self.a ** 2:
                    print('acute')
                if self.b ** 2 + self.c ** 2 < self.a ** 2:
                    print('obtuse')

            if self.b > self.a and self.b > self.c:
                if self.a ** 2 + self.c ** 2 == self.b ** 2:
                    print('right')
                if self.a ** 2 + self.c ** 2 > self.b ** 2:
                    print('acute')
                if self.a ** 2 + self.c ** 2 < self.b ** 2:
                    print('obtuse')

            if self.c > self.a and self.c > self.b:
                if self.a ** 2 + self.b ** 2 == self.c ** 2:
                    print('right')
                if self.a ** 2 + self.b ** 2 > self.c ** 2:
                    print('acute')
                if self.a ** 2 + self.b ** 2 < self.c ** 2:
                    print('obtuse')

            if self.a == self.b == self.c:
                print('acute')


def calculate_triangle_exist(a, b, c):
    num = Triangle(a, b, c)

    num.triangle_exist()


a = int(input())
b = int(input())
c = int(input())

calculate_triangle_exist(a, b, c)
