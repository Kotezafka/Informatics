class Coordinate:
    def __init__(self, crd1, crd2, crd3, crd4):
        self.crd1 = crd1
        self.crd2 = crd2
        self.crd3 = crd3
        self.crd4 = crd4

    def coordinate_quarters(self):
        if self.crd1 > 0 and self.crd2 > 0:
            if self.crd3 > 0 and self.crd4 > 0:
                print('YES')
            else:
                print('NO')

        if self.crd1 < 0 and self.crd2 > 0:
            if self.crd3 < 0 and self.crd4 > 0:
                print('YES')
            else:
                print('NO')

        if self.crd1 < 0 and self.crd2 < 0:
            if self.crd3 < 0 and self.crd4 < 0:
                print('YES')
            else:
                print('NO')

        if self.crd1 > 0 and self.crd2 < 0:
            if self.crd3 > 0 and self.crd4 < 0:
                print('YES')
            else:
                print('NO')


def calculate_coordinate_quarters(crd1, crd2, crd3, crd4):
    num = Coordinate(crd1, crd2, crd3, crd4)

    num.coordinate_quarters()


crd1 = int(input())
crd2 = int(input())
crd3 = int(input())
crd4 = int(input())

calculate_coordinate_quarters(crd1, crd2, crd3, crd4)
