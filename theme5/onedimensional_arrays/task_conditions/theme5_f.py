class Number:
    def __init__(self, n):
        self.n = n

    def number_elements_larger_both_neighboring(self):
        cnt = 0
        for i in range(1, self.n - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                cnt += 1
        print(cnt)


def calculate_number_elements_larger_both_neighboring(n):
    num = Number(n)

    return num.number_elements_larger_both_neighboring()


n = int(input())
A = list(map(int, input().split()))

calculate_number_elements_larger_both_neighboring(n)
