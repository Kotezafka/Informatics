class Symbols:
    def __init__(self, c):
        self.c = c

    def type_symbols(self):
        if type(self.c) == str:
            print('no')
        else:
            print('yes')


def calculate_type_symbols(c):
    num = Symbols(c)

    return num.type_symbols()

c = int(input())

calculate_type_symbols(c)
