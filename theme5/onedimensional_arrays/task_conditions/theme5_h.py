class Number:
    def __init__(self, n):
        self.n = n

    def transposition_neighboring_elements(self):
        k = str()
        if self.n % 2 == 0:
            m = self.n
        else:
            m = self.n - 1
        for i in range(0, m):
            if i % 2 == 0:
                A[i], A[i + 1] = A[i + 1], A[i]
        print(' '.join([str(a) for a in A]))


def calculate_transposition_neighboring_elements(n):
    num = Number(n)

    return num.transposition_neighboring_elements()


n = int(input())
A = list(map(int, input().split()))

calculate_transposition_neighboring_elements(n)
