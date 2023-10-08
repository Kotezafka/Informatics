def bowling(N: int, K: int) -> str:
    arr = ['I']*N
    for i in range(1, K + 1):
        pin = (input()).split()
        pin1 = int(pin[0])
        pin2 = int(pin[1])
        for j in range(pin1, pin2 + 1):
            arr[j - 1] = '.'
    return ''.join([str(a) for a in arr])


def calculate_bowling(N: int, K: int) -> None:
    new_arr = bowling(N, K)
    print(new_arr)


s = (input()).split()
N = int(s[0])
K = int(s[1])

calculate_bowling(N, K)
