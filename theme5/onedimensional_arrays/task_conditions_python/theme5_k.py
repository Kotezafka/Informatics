from typing import List


def amount_different_elements(arr: List[int]):
    cnt: int = 1
    number = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > number:
            cnt += 1
            number = arr[i]
    print(cnt)


def calculate_amount_different_elements(arr: List[int]):
    return amount_different_elements(arr)


arr = list(map(int, input().split()))

calculate_amount_different_elements(arr)
