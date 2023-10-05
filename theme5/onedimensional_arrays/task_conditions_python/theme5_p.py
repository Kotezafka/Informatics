from typing import List


def rearrange_min_and_max(arr: List[int]):
    min_element: int = arr[0]
    max_element: int = arr[0]
    serial_number1: int = 0
    serial_number2: int = 0

    for i in range(1, len(arr)):
        if arr[i] < min_element:
            min_element = arr[i]
            serial_number1 = i
        if arr[i] > max_element:
            max_element = arr[i]
            serial_number2 = i

    arr[serial_number1], arr[serial_number2] = arr[serial_number2], arr[serial_number1]

    return ' '.join([str(a) for a in arr])


def calculate_rearrange_min_and_max(arr: List[int]):
    new_arr = rearrange_min_and_max(arr)
    print(new_arr)


arr = list(map(int, input().split()))

calculate_rearrange_min_and_max(arr)
