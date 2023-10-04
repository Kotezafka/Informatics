from theme5.onedimensional_arrays.task_conditions.theme5_l import calculate_line

if __name__ == '__main__':
    number_of_students = int(input())
    A = list(map(int, input().split()))
    height = int(input())

    calculate_line(number_of_students, height)
