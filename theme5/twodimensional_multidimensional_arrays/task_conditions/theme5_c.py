from typing import List


def maximum_amount(n: int, matrix: List) -> str:
    answer = 'yes'
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][j] != matrix[j][i]:
                    answer = 'no'
                    break

    return answer


def calculate_maximum_amount(n: int, matrix: List) -> None:
    answer = maximum_amount(n, matrix)
    print(answer)


matrix = []
for i in range():
    value = (input()).split()
    value = [int(i) for i in value]
    matrix.append(value)

calculate_maximum_amount(n, matrix)
