class Time:
    def __init__(self, hour1, minute1, second1, hour2, minute2, second2):
        self.hour1 = hour1
        self.minute1 = minute1
        self.second1 = second1

        self.hour2 = hour2
        self.minute2 = minute2
        self.second2 = second2

    def time_difference(self):
        hours_in_seconds1 = self.hour1 * 3600
        minutes_in_seconds1 = self.minute1 * 60
        time_in_seconds1 = hours_in_seconds1 + minutes_in_seconds1 + self.second1

        hours_in_seconds2 = self.hour2 * 3600
        minutes_in_seconds2 = self.minute2 * 60
        time_in_seconds2 = hours_in_seconds2 + minutes_in_seconds2 + self.second2

        difference = time_in_seconds2 - time_in_seconds1

        print(difference)


def calculate_time_difference(hour1, minute1, second1, hour2, minute2, second2):
    num = Time(hour1, minute1, second1, hour2, minute2, second2)

    num.time_difference()


hour1 = int(input())
minute1 = int(input())
second1 = int(input())

hour2 = int(input())
minute2 = int(input())
second2 = int(input())

calculate_time_difference(hour1, minute1, second1, hour2, minute2, second2)
