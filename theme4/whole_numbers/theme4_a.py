class Number:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def max_number_of_rabbits(self):
        if self.m % self.n != 0:
            number_rabbits = self.m // self.n
            max_number_rabbits = number_rabbits + 1

        elif self.n == self.m:
            max_number_rabbits = 1

        else:
            max_number_rabbits = self.m // self.n

        return max_number_rabbits


def calculate_max_number_of_rabbits(n, m):
    num = Number(n, m)

    return num.max_number_of_rabbits()

s = (input()).split()
n = int(s[0])
m = int(s[1])

a = calculate_max_number_of_rabbits(n, m)
print(a)
