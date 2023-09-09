class Time:
    def __init__(self, d):
        self.d = d

    def hours_and_minutes(self):
        hours = 0
        minutes = 0
        if self.d >= 30:
            hours = self.d // 30
            hours_in_degrees = 30 * hours
            remainder = self.d - hours_in_degrees
            minutes = remainder * 2
        else:
            hours = 0
            minutes = self.d * 2
        print('It is', hours, 'hours', minutes, 'minutes.')


def calculate_hours_and_minutes(d):
    num = Time(d)

    num.hours_and_minutes()


d = int(input())

calculate_hours_and_minutes(d)
