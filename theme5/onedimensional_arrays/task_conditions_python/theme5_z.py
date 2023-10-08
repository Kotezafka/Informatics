from typing import List


def shift_by_k_elements(arr: List[int], k: int) -> str:
    k = k % len(arr)
    if k > 0:
        arr = arr[-k:] + arr[0:len(arr)-k]
    elif k < 0:
        arr = arr[-abs(k)+1:] + arr[0:abs(k)]
    return ' '.join([str(a) for a in arr])


def calculate_shift_by_k_elements(arr: List[int], k: int) -> None:
    new_arr = shift_by_k_elements(arr, k)
    print(new_arr)


arr = list(map(int, input().split()))
k = int(input())

calculate_shift_by_k_elements(arr, k)
