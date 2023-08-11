class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def exists_triangle(self):
        if self.side1 + self.side2 > self.side3 and self.side2 + self.side3 > self.side1 and self.side1 + self.side3 > self.side2:
            print('YES')
        else:
            print('NO')


def calculate_exists_triangle(side1, side2, side3):
    num = Triangle(side1, side2, side3)

    num.exists_triangle()


side1 = int(input())
side2 = int(input())
side3 = int(input())

calculate_exists_triangle(side1, side2, side3)
