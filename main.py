from theme3.operator_for.task_conditions.theme3_х_digit_in_number import calculate_digit_in_number

if __name__ == '__main__':
    x = int(input())
    d = int(input())

    n = calculate_digit_in_number(x, d)
    print(n)
