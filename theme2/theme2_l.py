class Chocolate:
    def __init__(self, length, width, slice):
        self.length = length
        self.width = width
        self.slice = slice

    def break_off_the_slices(self):
        if self.slice % self.length == 0 or self.slice % self.width == 0:
            print('YES')
        else:
            print('NO')


def calculate_break_off_the_slices(length, width, slice):
    num = Chocolate(length, width, slice)

    num.break_off_the_slices()


length = int(input())
width = int(input())
slice = int(input())

calculate_break_off_the_slices(length, width, slice)
