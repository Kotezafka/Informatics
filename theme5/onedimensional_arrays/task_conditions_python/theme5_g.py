def largest_element(A):
    max_element = A[0]
    index = 0
    for i in range(1, len(A)):
        if A[i] > max_element:
            max_element = A[i]
            index = i
    print(max_element, index, end=' ')


def calculate_largest_element(A):
    return largest_element(A)


A = list(map(int, input().split()))

calculate_largest_element(A)
