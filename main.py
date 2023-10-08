from theme5.onedimensional_arrays.task_conditions_python.theme5_x import calculate_bowling

if __name__ == '__main__':
    s = (input()).split()
    N = int(s[0])
    K = int(s[1])

    calculate_bowling(N, K)
