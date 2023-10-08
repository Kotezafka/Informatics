from theme5.onedimensional_arrays.task_conditions.theme5_n import calculate_shift_by_k_elements

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    k = int(input())

    calculate_shift_by_k_elements(n, A, k)
