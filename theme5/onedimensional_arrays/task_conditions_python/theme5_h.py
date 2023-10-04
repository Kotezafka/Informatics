from typing import List


def smallest_positive_element(arr: List[int]):
    min_positive_element: int = 1000
    for i in range(0, len(arr)):
        if (arr[i] < min_positive_element) and (arr[i] > 0):
            min_positive_element = arr[i]
    print(min_positive_element)


def calculate_smallest_positive_element(arr: List[int]):
    return smallest_positive_element(arr)


arr = list(map(int, input().split()))

calculate_smallest_positive_element(arr)
