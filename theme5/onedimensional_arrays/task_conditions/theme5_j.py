class Number:
    def __init__(self, n):
        self.n = n

    def maximum_in_array(self):
        max_element = A[0]
        for i in range(0, self.n):
            if A[i] > max_element:
                max_element = A[i]
        print(max_element)


def calculate_maximum_in_array(n):
    num = Number(n)

    return num.maximum_in_array()


n = int(input())
A = list(map(int, input().split()))

calculate_maximum_in_array(n)
