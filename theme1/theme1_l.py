class Number:
    def __init__(self, number):
        self.number = number

    def time_on_the_clock(self):
        number_of_full_hours = self.number // 3600
        number_of_hours_on_the_clock = number_of_full_hours % 24
        hours_in_seconds = number_of_full_hours * 3600
        remainder = self.number - hours_in_seconds

        if remainder < 60:
            number_of_full_seconds = remainder
            number_of_second_on_the_clock = number_of_full_seconds
            number_of_minutes_on_the_clock = 0

        else:
            number_of_full_minutes = remainder // 60
            number_of_minutes_on_the_clock = number_of_full_minutes
            minutes_in_seconds = number_of_full_minutes * 60
            number_of_full_seconds = remainder - minutes_in_seconds
            number_of_second_on_the_clock = number_of_full_seconds

        print(number_of_hours_on_the_clock, ':', end='', sep='')

        if number_of_minutes_on_the_clock < 10:
            print('0', number_of_minutes_on_the_clock, ':', end='', sep='')

        else:
            print(number_of_minutes_on_the_clock, ':', end='', sep='')

        if number_of_second_on_the_clock < 10:
            print('0', number_of_second_on_the_clock, end='', sep='')

        else:
            print(number_of_second_on_the_clock, end='', sep='')


def calculate_time_on_the_clock(number):
    num = Number(number)

    num.time_on_the_clock()


number = int(input())

calculate_time_on_the_clock(number)
