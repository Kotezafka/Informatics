class Number:
    def __init__(self, n):
        self.n = n

    def identical_signs(self):
        k = str()
        for i in range(1, self.n):
            if (A[i - 1] > 0 and A[i] > 0) or (A[i - 1] < 0 and A[i] < 0):
                k = 'YES'
                break
            else:
                k = 'NO'
        print(k)


def calculate_identical_signs(n):
    num = Number(n)

    return num.identical_signs()


n = int(input())
A = list(map(int, input().split()))

calculate_identical_signs(n)
