class Name:
    def __init__(self, students, amount_of_apples):
        self.students = students
        self.amount_of_apples = amount_of_apples

    def division_of_apples(self):
        return (self.amount_of_apples % self.students != 0) * (self.students - self.amount_of_apples % self.students) + (self.amount_of_apples % self.students == 0) * (self.amount_of_apples % self.students)


def calculate_division_of_apples(students, amount_of_apples):
    num = Name(students, amount_of_apples)

    a = num.division_of_apples()
    print(a)


students = int(input())
amount_of_apples = int(input())

calculate_division_of_apples(students, amount_of_apples)
