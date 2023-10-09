from typing import List


def output_in_reverse_order(arr: List[int]) -> str:
    for i in range(0, len(arr) // 2):
        arr[i], arr[len(arr) - (i + 1)] = arr[len(arr) - (i + 1)], arr[i]
    return ' '.join([str(a) for a in arr])


def calculate_output_in_reverse_order(arr: List[int]) -> None:
    new_arr = output_in_reverse_order(arr)
    print(new_arr)


arr = list(map(int, input().split()))

calculate_output_in_reverse_order(arr)
