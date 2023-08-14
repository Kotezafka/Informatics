class Purchase:
    def __init__(self, ruble1, penny1, ruble2, penny2):
        self.ruble1 = ruble1
        self.penny1 = penny1
        self.ruble2 = ruble2
        self.penny2 = penny2

    def change(self):
        rubles1_to_penny = self.ruble1 * 100
        rubles2_to_penny = self.ruble2 * 100

        purchase_price = rubles1_to_penny + self.penny1
        paid = rubles2_to_penny + self.penny2

        change = paid - purchase_price
        change_in_rubles = change // 100
        change_in_penny = change % 100

        print(change_in_rubles, change_in_penny)


def calculate_change(ruble1, penny1, ruble2, penny2):
    num = Purchase(ruble1, penny1, ruble2, penny2)

    num.change()


ruble1 = int(input())
penny1 = int(input())
ruble2 = int(input())
penny2 = int(input())

calculate_change(ruble1, penny1, ruble2, penny2)
