from typing import List


def amount_identical_pairs(arr: List[int]) -> int:
    amount = 0
    k = 0
    for i in range(0, len(arr) - 1):
        k += 1

        n = 0
        for j in range(k, len(arr)):
            if arr[i] == arr[j]:
                amount += 1
            k += 1
            n += 1
        k = k - n
    return amount


def calculate_amount_identical_pairs(arr: List[int]) -> None:
    amount = amount_identical_pairs(arr)
    print(amount)


arr = list(map(int, input().split()))

calculate_amount_identical_pairs(arr)
