from typing import List


def side_diagonal(n: int) -> List:
    arr = []
    for i in range(n):
        arr.append([0] * n)

    for i in range(n):
        for j in range(n):
            if i + j == n - 1:
                arr[i][j] = 1
            elif i + j < n - 1:
                arr[i][j] = 0
            else:
                arr[i][j] = 2

    return arr


def calculate_side_diagonal(n: int) -> None:
    new_arr = side_diagonal(n)
    for inner_list in new_arr:
        print(' '.join(str(a) for a in inner_list))
    # for i in range(n):
    #     for j in range(n):
    #         print(new_arr[i][j], end=' ')
    #     print('')


n = int(input())

calculate_side_diagonal(n)
