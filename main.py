from theme5.onedimensional_arrays.task_conditions.theme5_b import calculate_output_even_elements

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))

    calculate_output_even_elements(n)
