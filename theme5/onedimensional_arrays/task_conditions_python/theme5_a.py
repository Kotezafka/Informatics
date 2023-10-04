def output_even_array_elements(A):
    for i in range(len(A)):
        if i % 2 == 0:
            print(A[i], end=' ')


def calculate_output_even_array_elements(A):
    return output_even_array_elements(A)


A = list(map(int, input().split()))

calculate_output_even_array_elements(A)
