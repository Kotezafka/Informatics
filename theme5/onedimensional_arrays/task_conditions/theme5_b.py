class Number:
    def __init__(self, n):
        self.n = n

    def output_even_elements(self):
        for i in range(0, self.n):
            if A[i] % 2 == 0:
                print(A[i], end=' ')


def calculate_output_even_elements(n):
    num = Number(n)

    return num.output_even_elements()


n = int(input())
A = list(map(int, input().split()))

calculate_output_even_elements(n)
