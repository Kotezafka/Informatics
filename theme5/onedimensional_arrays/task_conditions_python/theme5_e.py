def pair_numbers_same_sign(A):
    for i in range(len(A) - 1):
        if (A[i] >= 0 and A[i + 1] >= 0) or (A[i] < 0 and A[i + 1] < 0):
            print(A[i], A[i + 1], end=' ')
            break


def calculate_pair_numbers_same_sign(A):
    return pair_numbers_same_sign(A)


A = list(map(int, input().split()))

calculate_pair_numbers_same_sign(A)
