def element_that_larger_previous(A):
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            print(A[i], end=' ')


def calculate_element_that_larger_previous(A):
    return element_that_larger_previous(A)


A = list(map(int, input().split()))

calculate_element_that_larger_previous(A)
