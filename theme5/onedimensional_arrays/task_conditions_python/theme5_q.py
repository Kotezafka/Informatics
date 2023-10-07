from typing import List


def remove_element(arr: List[int], k: int) -> str:
    arr.pop(k)
    return ' '.join([str(a) for a in arr])


def calculate_remove_element(arr: List[int], k: int) -> None:
    new_arr = remove_element(arr, k)
    print(new_arr)


arr = list(map(int, input().split()))
k = int(input())

calculate_remove_element(arr, k)
