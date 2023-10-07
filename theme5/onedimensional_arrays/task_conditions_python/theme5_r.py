from typing import List


def insert_element(arr: List[int], k: int, C: int) -> str:
    part1 = arr[:k]
    part1.append(C)
    part2 = arr[k:]
    arr = part1 + part2

    return ' '.join([str(a) for a in arr])


def calculate_insert_element(arr: List[int], k: int, C: int) -> None:
    new_arr = insert_element(arr, k, C)
    print(new_arr)


arr = list(map(int, input().split()))

s = (input()).split()
k = int(s[0])
C = int(s[1])

calculate_insert_element(arr, k, C)
