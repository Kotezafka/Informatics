class Ticket:
    def __init__(self, number_of_trips):
        self.number_of_trips = number_of_trips

    def number_of_tickets(self):
        tickets_for_1_trips = 0
        tickets_for_10_trips = 0
        tickets_for_60_trips = 0

        tickets_for_60_trips = self.number_of_trips // 60
        trips_left1 = self.number_of_trips % 60

        if trips_left1 >= 30:
            tickets_for_60_trips += 1

        if trips_left1 < 30:
            tickets_for_10_trips = trips_left1 // 10
            trips_left2 = trips_left1 % 10

            if trips_left2 == 9:
                tickets_for_10_trips += 1
            else:
                tickets_for_1_trips = trips_left2

        print(tickets_for_1_trips, tickets_for_10_trips, tickets_for_60_trips)


def calculate_number_of_tickets(number_of_trips):
    num = Ticket(number_of_trips)

    num.number_of_tickets()


number_of_trips = int(input())

calculate_number_of_tickets(number_of_trips)
