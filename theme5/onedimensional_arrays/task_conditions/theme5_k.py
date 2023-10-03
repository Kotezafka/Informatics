class Number:
    def __init__(self, n):
        self.n = n

    def amount_different_elements(self):
        cnt = 1
        for i in range(0, self.n - 1):
            if A[i] < A[i + 1]:
                cnt += 1
        print(cnt)


def calculate_amount_different_elements(n):
    num = Number(n)

    return num.amount_different_elements()


n = int(input())
A = list(map(int, input().split()))

calculate_amount_different_elements(n)
