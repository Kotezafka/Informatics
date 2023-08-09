class Car:
    def __init__(self, kilometers_in_one_day, way_in_kilometers):
        self.kilometers_in_one_day = kilometers_in_one_day
        self.way_in_kilometers = way_in_kilometers

    def amount_of_days(self):
        days = ((self.way_in_kilometers - 1) // self.kilometers_in_one_day) + 1

        print(days)


def calculate_amount_of_days(kilometers_in_one_day, way_in_kilometers):
    num = Car(kilometers_in_one_day, way_in_kilometers)

    num.amount_of_days()


kilometers_in_one_day = int(input())
way_in_kilometers = int(input())

calculate_amount_of_days(kilometers_in_one_day, way_in_kilometers)
