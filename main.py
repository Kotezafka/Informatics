from theme5.onedimensional_arrays.task_conditions.theme5_k import calculate_amount_different_elements

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    calculate_amount_different_elements(n)
