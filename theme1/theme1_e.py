class Way:
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time

    def remainder(self):
        a = (self.speed * self.time) % 109
        return a


def mark(speed, time):
    way = Way(speed, time)

    return way.remainder()


speed = int(input())
time = int(input())

a = mark(speed, time)
print(a)
