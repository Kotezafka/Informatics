class Number:
    def __init__(self, n):
        self.n = n

    def amount_positive_elements(self):
        cnt = 0
        for i in range(0, self.n):
            if A[i] > 0:
                cnt += 1
        print(cnt)


def calculate_amount_positive_elements(n):
    num = Number(n)

    return num.amount_positive_elements()


n = int(input())
A = list(map(int, input().split()))

calculate_amount_positive_elements(n)
