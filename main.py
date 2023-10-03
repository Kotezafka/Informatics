from theme5.onedimensional_arrays.task_conditions.theme5_h import calculate_transposition_neighboring_elements

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    calculate_transposition_neighboring_elements(n)
