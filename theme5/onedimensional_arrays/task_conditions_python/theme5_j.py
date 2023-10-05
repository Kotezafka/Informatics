from typing import List


def line(arr: List[int]):
    cnt = 1
    for i in range(0, len(arr)):
        if arr[i] >= height:
            cnt += 1
    print(cnt)


def calculate_line(arr: List[int]):
    return line(arr)


arr = list(map(int, input().split()))
height = int(input())

calculate_line(arr)
