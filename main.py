from theme5.onedimensional_arrays.task_conditions_python.theme5_r import calculate_insert_element

if __name__ == '__main__':
    arr = list(map(int, input().split()))

    s = (input()).split()
    k = int(s[0])
    C = int(s[1])

    calculate_insert_element(arr, k, C)
