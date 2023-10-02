class Number:
    def __init__(self, n):
        self.n = n

    def amount_elements_greater_previous(self):
        cnt = 0
        i = 0
        while i < self.n - 1:
            i += 1
            if A[i] > A[i - 1]:
                cnt += 1
        print(cnt)


def calculate_amount_elements_greater_previous(n):
    num = Number(n)

    return num.amount_elements_greater_previous()


n = int(input())
A = list(map(int, input().split()))

calculate_amount_elements_greater_previous(n)
