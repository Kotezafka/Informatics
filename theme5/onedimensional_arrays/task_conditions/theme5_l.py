class Number:
    def __init__(self, number_of_students, height):
        self.number_of_students = number_of_students
        self.height = height

    def line(self):
        cnt = 1
        for i in range(0, self.number_of_students):
            if A[i] >= self.height:
                cnt += 1
        print(cnt)


def calculate_line(number_of_students, height):
    num = Number(number_of_students, height)

    return num.line()


number_of_students = int(input())
A = list(map(int, input().split()))
height = int(input())

calculate_line(number_of_students, height)
