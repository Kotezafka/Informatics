from typing import List


def smallest_odd_element(arr: List[int]):
    min_odd_element: int = 1000
    for i in range(0, len(arr)):
        if (arr[i] < min_odd_element) and (arr[i] % 2 != 0):
            min_odd_element = arr[i]
    if min_odd_element == 1000:
        min_odd_element = 0
    print(min_odd_element)


def calculate_smallest_odd_element(arr: List[int]):
    return smallest_odd_element(arr)


arr = list(map(int, input().split()))

calculate_smallest_odd_element(arr)
