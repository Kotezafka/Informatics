class Snail:
    def __init__(self, tree_height, climb, descent):
        self.tree_height = tree_height
        self.climb = climb
        self.descent = descent

    def amount_of_days(self):
        height_before_last_climb = self.tree_height - self.climb
        all_days = (height_before_last_climb - 1) // (self.climb - self.descent) + 2

        print(all_days)


def calculate_amount_of_days(tree_height, climb, descent):
    num = Snail(tree_height, climb, descent)

    num.amount_of_days()


tree_height = int(input())
climb = int(input())
descent = int(input())

calculate_amount_of_days(tree_height, climb, descent)
