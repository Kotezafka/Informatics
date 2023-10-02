from theme5.onedimensional_arrays.task_conditions.theme5_f import calculate_number_elements_larger_both_neighboring

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    calculate_number_elements_larger_both_neighboring(n)
