class Name:
    def __init__(self, students, amount_of_apples):
        self.students = students
        self.amount_of_apples = amount_of_apples

    def division_of_apples(self):
        students_with_fewer_apples = self.students - self.amount_of_apples % self.students

        print(students_with_fewer_apples)


def calculate_division_of_apples(students, amount_of_apples):
    num = Name(students, amount_of_apples)

    num.division_of_apples()
