from typing import List


def cyclic_shift_right(arr: List[int]):
    if len(arr) == 1:
        print(arr[0])
    else:
        for i in range(1, len(arr) - 1):
            arr[1], arr[i + 1] = arr[i + 1], arr[1]
        arr[0], arr[1] = arr[1], arr[0]
        print(' '.join([str(a) for a in arr]))


def calculate_cyclic_shift_right(arr: List[int]):
    return cyclic_shift_right(arr)


arr = list(map(int, input().split()))

calculate_cyclic_shift_right(arr)
