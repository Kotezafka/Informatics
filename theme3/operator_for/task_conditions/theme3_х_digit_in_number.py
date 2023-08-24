class Number:
    def __init__(self, x, d):
        self.x = x
        self.d = d

    def digit_in_number(self):
        m = 0
        t = self.x
        while t != 0:
            if t % 10 == self.d:
                m += 1
            t = t // 10
        return m


def calculate_digit_in_number(x, d):
    num = Number(x, d)

    return num.digit_in_number()


x = int(input())
d = int(input())

n = calculate_digit_in_number(x, d)
print(n)
