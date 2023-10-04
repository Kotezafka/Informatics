def element_larger_neighbors(A):
    cnt = 0
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            cnt += 1
    print(cnt)


def calculate_element_larger_neighbors(A):
    return element_larger_neighbors(A)


A = list(map(int, input().split()))

calculate_element_larger_neighbors(A)
