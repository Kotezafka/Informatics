from theme5.twodimensional_multidimensional_arrays.task_conditions.theme5_b import calculate_matrix_symmetry

if __name__ == '__main__':
    n = int(input())

    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            value = int(input(({i}, {j})))
            row.append(value)
        matrix.append(row)

    calculate_matrix_symmetry(n, matrix)
