class Chess:
    def __init__(self, coordinates1, coordinates2, coordinates3, coordinates4):
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2
        self.coordinates3 = coordinates3
        self.coordinates4 = coordinates4

    def step(self):
        if self.coordinates1 == self.coordinates3 and abs(self.coordinates4 - self.coordinates2) == 1 or self.coordinates2 == self.coordinates4 and abs(self.coordinates3 - self.coordinates1) == 1 or abs(self.coordinates3 - self.coordinates1) == abs(self.coordinates4 - self.coordinates2) and abs(self.coordinates4 - self.coordinates2) == 1 and abs(self.coordinates3 - self.coordinates1) == 1:
            print('YES')
        else:
            print('NO')


def calculate_step(coordinates1, coordinates2, coordinates3, coordinates4):
    num = Chess(coordinates1, coordinates2, coordinates3, coordinates4)

    num.step()


coordinates1 = int(input())
coordinates2 = int(input())
coordinates3 = int(input())
coordinates4 = int(input())

calculate_step(coordinates1, coordinates2, coordinates3, coordinates4)
