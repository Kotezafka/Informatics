def amount_positive_elements(A):
    cnt = 0
    for i in range(len(A)):
        if A[i] > 0:
            cnt += 1
    print(cnt)


def calculate_amount_positive_elements(A):
    return amount_positive_elements(A)


A = list(map(int, input().split()))

calculate_amount_positive_elements(A)
