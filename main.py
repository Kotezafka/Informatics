from theme1.theme1_s import calculate_amount_of_days

if __name__ == '__main__':
    tree_height = int(input())
    climb = int(input())
    descent = int(input())

    calculate_amount_of_days(tree_height, climb, descent)
