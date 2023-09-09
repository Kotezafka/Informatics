class Time:
    def __init__(self, k):
        self.k = k

    def hours_and_minutes(self):
        if self.k >= 3600:
            hours = self.k // 3600
            hours_in_seconds = 3600 * hours
            remainder = self.k - hours_in_seconds
            minutes = remainder // 60
        else:
            hours = 0
            minutes = self.k // 60
        print('It is', hours, 'hours', minutes, 'minutes.')


def calculate_hours_and_minutes(k):
    num = Time(k)

    num.hours_and_minutes()


k = int(input())

calculate_hours_and_minutes(k)
