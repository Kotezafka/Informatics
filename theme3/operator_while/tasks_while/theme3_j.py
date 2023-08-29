class Number:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def algorithm(self):
        k = self.a
        while k > self.b:
            if k % 2 == 0:
                if k // 2 > self.b:
                    k = k // 2
                    print(':2')
                else:
                    k = k - 1
                    print('-1')
            else:
                k = k - 1
                print('-1')


def find_algorithm(a, b):
    num = Number(a, b)

    num.algorithm()


a = int(input())
b = int(input())

find_algorithm(a, b)
