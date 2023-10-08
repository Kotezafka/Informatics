from typing import List


def list_compression(arr: List[int]) -> str:
    serial_number = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[serial_number] = arr[serial_number], arr[i]
            serial_number += 1
    return ' '.join([str(a) for a in arr])


def calculate_list_compression(arr: List[int]) -> None:
    new_arr = list_compression(arr)
    print(new_arr)


arr = list(map(int, input().split()))

calculate_list_compression(arr)
