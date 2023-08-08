from theme1.theme1_o import calculate_purchase_price

if __name__ == '__main__':
    rubles = int(input())
    pennies = int(input())
    quantity = int(input())

    calculate_purchase_price(rubles, pennies, quantity)
