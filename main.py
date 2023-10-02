from theme5.onedimensional_arrays.task_conditions.theme5_d import calculate_amount_elements_greater_previous

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    calculate_amount_elements_greater_previous(n)
