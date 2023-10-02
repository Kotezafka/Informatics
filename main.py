from theme5.onedimensional_arrays.task_conditions.theme5_c import calculate_amount_positive_elements

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    calculate_amount_positive_elements(n)
