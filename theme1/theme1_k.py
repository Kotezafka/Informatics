class Number:
    def __init__(self, number):
        self.number = number

    def time_on_the_clock(self):
        number_of_full_hours = self.number // 60
        number_of_minutes = number_of_full_hours * 60

        number_of_hours_on_the_clock = number_of_full_hours % 24
        number_of_minutes_on_the_clock = self.number - number_of_minutes

        print(number_of_hours_on_the_clock, number_of_minutes_on_the_clock)


def calculate_time_on_the_clock(number):
    num = Number(number)

    num.time_on_the_clock()


number = int(input())

calculate_time_on_the_clock(number)
