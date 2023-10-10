def filling_snake(n: int, m: int) -> list:
    arr = [[0] * m for _ in range(n)]

    k = 0
    for i in range(0, n):
        if i % 2 == 0:
            for j in range(0, m):
                arr[n][m] = k
                k += 1
        else:
            for j in range(m, -1, -1):
                arr[n][m] = k
                k += 1

    return arr


def calculate_filling_snake(n: int, m: int) -> None:
    new_arr = filling_snake(n, m)
    for inner_list in new_arr:
        print(' '.join(str(a) for a in inner_list))


s = (input()).split()
n = int(s[0])
m = int(s[1])

calculate_filling_snake(n, m)
