class Pie:
    def __init__(self, rubles, pennies, quantity):
        self.rubles = rubles
        self.pennies = pennies
        self.quantity = quantity

    def purchase_price(self):
        rubles_to_pennies = self.rubles * 100
        cost_in_pennies = rubles_to_pennies + self.pennies
        cost_of_pies = cost_in_pennies * self.quantity

        number_of_rubles = cost_of_pies // 100
        number_of_pennies = cost_of_pies % 100

        print(number_of_rubles, number_of_pennies)


def calculate_purchase_price(rubles, pennies, quantity):
    num = Pie(rubles, pennies, quantity)

    num.purchase_price()


rubles = int(input())
pennies = int(input())
quantity = int(input())

calculate_purchase_price(rubles, pennies, quantity)
