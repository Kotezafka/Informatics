class Number:
    def __init__(self, n):
        self.n = n

    def array_elements_reverse_order(self):
        k = str()
        for i in range(-1, -self.n - 1, -1):
            k += str(A[i]) + ' '
        print(k)


def calculate_array_elements_reverse_order(n):
    num = Number(n)

    return num.array_elements_reverse_order()


n = int(input())
A = list(map(int, input().split()))

calculate_array_elements_reverse_order(n)
