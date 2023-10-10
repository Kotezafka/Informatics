def side_diagonal(n: int) -> list:
    arr = []
    for i in range(n):
        arr.append([0] * n)

    for i in range(0, n):
        for j in range(0, n):
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


n = int(input())

calculate_side_diagonal(n)
