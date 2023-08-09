class Number:
    def __init__(self, number_of_lessons_passed):
        self.number_of_lessons_passed = number_of_lessons_passed

    def time_on_the_clock(self):
        lesson_time = self.number_of_lessons_passed * 45
        number_of_even_breaks = (self.number_of_lessons_passed - 1) // 2
        number_of_odd_breaks = self.number_of_lessons_passed // 2

        time_of_even_breaks = number_of_even_breaks * 15
        time_of_odd_breaks = number_of_odd_breaks * 5

        total_time = lesson_time + time_of_even_breaks + time_of_odd_breaks

        number_of_full_hours = total_time // 60
        number_of_hours_on_the_clock = 9 + number_of_full_hours
        hours_in_minutes = number_of_full_hours * 60

        number_of_minutes = total_time - hours_in_minutes
        number_of_minutes_on_the_clock = 0 + number_of_minutes

        print(number_of_hours_on_the_clock, number_of_minutes_on_the_clock)


def calculate_time_on_the_clock(number_of_lessons_passed):
    num = Number(number_of_lessons_passed)

    num.time_on_the_clock()


number_of_lessons_passed = int(input())

calculate_time_on_the_clock(number_of_lessons_passed)
