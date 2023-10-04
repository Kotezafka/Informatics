def shift_by_k_elements(n, A, k):
    if k >= 0:
        A = A[-k:] + A[0:n-k]
    else:
        A = A[-abs(k)+1:] + A[0:abs(k)]
    print(' '.join(str(a) for a in A))


def calculate_shift_by_k_elements(n, A, k):
    return shift_by_k_elements(n, A, k)


n = int(input())
A = list(map(int, input().split()))
k = int(input())

calculate_shift_by_k_elements(n, A, k)
