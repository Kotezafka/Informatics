from typing import List


def rearrangement_of_adjacent_elements(arr: List[int]) -> str:
    x = 2 if len(arr) % 2 != 0 else 1
    for i in range(0, len(arr) - x, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return ' '.join([str(a) for a in arr])


def calculate_rearrangement_of_adjacent_elements(arr: List[int]) -> None:
    new_arr = rearrangement_of_adjacent_elements(arr)
    print(new_arr)


arr = list(map(int, input().split()))

calculate_rearrangement_of_adjacent_elements(arr)
