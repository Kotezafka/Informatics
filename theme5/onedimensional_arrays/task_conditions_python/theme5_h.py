def smallest_positive_element(A):
    min_positive_element = 1000
    for i in range(1, len(A)):
        if (A[i] < min_positive_element) and (A[i] > 0):
            min_positive_element = A[i]
    print(min_positive_element)


def calculate_smallest_positive_element(A):
    return smallest_positive_element(A)


A = list(map(int, input().split()))

calculate_smallest_positive_element(A)
