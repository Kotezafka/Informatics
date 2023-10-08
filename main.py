from theme5.onedimensional_arrays.task_conditions_python.theme5_z import calculate_shift_by_k_elements

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    k = int(input())

    calculate_shift_by_k_elements(arr, k)
