class Number:
    def __init__(self, n):
        self.n = n

    def cyclic_shift_right(self):
        if self.n == 1:
            print(A[0])
        else:
            for i in range(1, self.n - 1):
                A[1], A[i + 1] = A[i + 1], A[1]
            A[0], A[1] = A[1], A[0]
            print(' '.join([str(a) for a in A]))


def calculate_cyclic_shift_right(n):
    num = Number(n)

    return num.cyclic_shift_right()


n = int(input())
A = list(map(int, input().split()))

calculate_cyclic_shift_right(n)
