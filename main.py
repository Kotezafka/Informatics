from theme1.theme1_p import calculate_time_difference

if __name__ == '__main__':
    hour1 = int(input())
    minute1 = int(input())
    second1 = int(input())
    hour2 = int(input())
    minute2 = int(input())
    second2 = int(input())

    calculate_time_difference(hour1, minute1, second1, hour2, minute2, second2)
