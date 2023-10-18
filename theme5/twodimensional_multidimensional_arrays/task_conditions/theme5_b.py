from typing import List


def matrix_symmetry(n: int, matrix: List) -> str:
    answer = 'yes'
    for i in range(n):
        for j in range(n):
            if i != j:
                if matrix[i][j] != matrix[j][i]:
                    answer = 'no'
                    break

    return answer


def calculate_matrix_symmetry(n: int, matrix: List) -> None:
    answer = matrix_symmetry(n, matrix)
    print(answer)


n = int(input())

matrix = []
for i in range(n):
    value = (input()).split()
    value = [int(i) for i in value]
    matrix.append(value)

calculate_matrix_symmetry(n, matrix)
