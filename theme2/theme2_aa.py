class Coordinates:
    def __init__(self, m, n, x, y):
        self.m = m
        self.n = n
        self.x = x
        self.y = y

    def coordinates_neighbors(self):
        if self.m == 1 and self.n == 1 and self.x == 1 and self.y == 1:
            print('')
        else:
            if self.m == 2 and self.n == 1:
                if self.x == 2:
                    print(f'{self.x - 1} {self.y}')
                if self.x == 1:
                    print(f'{self.x + 1} {self.y}')

            elif self.m == 1 and self.n == 2:
                if self.y == 2:
                    print(f'{self.x} {self.y - 1}')
                if self.y == 1:
                    print(f'{self.x} {self.y + 1}')

            # elif self.m == 3 and self.n == 1:
            #     if self.x == 3:
            #         print(f'{self.}')
            #
            # if self.m == 1 and self.n == 3:


            else:
                if self.x < self.m and self.x != 1 and self.y < self.n and self.y != 1:
                    print(f'{self.x} {self.y - 1}\n{self.x - 1} {self.y}\n{self.x} {self.y + 1}\n{self.x + 1} {self.y}')

                if self.x == self.m and self.y != 1 and self.y < self.n:
                    print(f'{self.x} {self.y - 1}\n{self.x - 1} {self.y}\n{self.x} {self.y + 1}')

                if self.y == self.n and self.x != 1 and self.x < self.m:
                    print(f'{self.x} {self.y - 1}\n{self.x - 1} {self.y}\n{self.x + 1} {self.y}')

                if self.x == 1 and self.y != 1 and self.y < self.n:
                    print(f'{self.x} {self.y - 1}\n{self.x + 1} {self.y}\n{self.x} {self.y + 1}')

                if self.y == 1 and self.x != 1 and self.x < self.m:
                    print(f'{self.x - 1} {self.y}\n{self.x} {self.y + 1}\n{self.x + 1} {self.y}')

                if self.x == self.m:
                    if self.y == self.n:
                        print(f'{self.x} {self.y - 1}\n{self.x - 1} {self.y}')
                    if self.y == 1:
                        print(f'{self.x - 1} {self.y}\n{self.x} {self.y + 1}')

                if self.x == 1:
                    if self.y == self.n:
                        print(f'{self.x} {self.y - 1}\n{self.x + 1} {self.y}')
                    if self.y == 1:
                        print(f'{self.x} {self.y + 1}\n{self.x + 1} {self.y}')


def calculate_coordinates_neighbors(m, n, x, y):
    num = Coordinates(m, n, x, y)

    num.coordinates_neighbors()


s1 = input().split()
s2 = input().split()

m = int(s1[0])
n = int(s1[1])
x = int(s2[0])
y = int(s2[1])

calculate_coordinates_neighbors(m, n, x, y)
