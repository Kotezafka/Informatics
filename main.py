from theme4.whole_numbers.theme4_a import calculate_max_number_of_rabbits

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    a = calculate_max_number_of_rabbits(n, m)
    print(a)
