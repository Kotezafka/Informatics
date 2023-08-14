class Square_board:
    def __init__(self, number_of_chips):
        self.number_of_chips = number_of_chips

    def amount_chips(self):
        if self.number_of_chips % 4 == 0 or self.number_of_chips == 1:
            print('YES')
        else:
            print('NO')


def calculate_amount_chips(number_of_chips):
    num = Square_board(number_of_chips)

    num.amount_chips()


number_of_chips = int(input())

calculate_amount_chips(number_of_chips)
