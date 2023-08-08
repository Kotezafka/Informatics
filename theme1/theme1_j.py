class Number:
    def __init__(self, number):
        self.number = number

    def next_even(self):
        next_number = self.number + 1
        remainder_of_the_division = next_number % 2
        even_number = next_number + remainder_of_the_division

        return even_number


def calculate_next_even(number):
    num = Number(number)

    return num.next_even()


number = int(input())

even_number = calculate_next_even(number)
print(even_number)
