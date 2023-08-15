class Ice_cream:
    def __init__(self, ice_cream_balls):
        self.ice_cream_balls = ice_cream_balls

    def purchase_opportunity(self):
        if self.ice_cream_balls >= 8:
            print('YES')
        elif self.ice_cream_balls < 8:
            if self.ice_cream_balls % 3 == 0 or self.ice_cream_balls % 5 == 0:
                print('YES')
            else:
                print('NO')


def calculate_purchase_opportunity(ice_cream_balls):
    num = Ice_cream(ice_cream_balls)

    num.purchase_opportunity()


ice_cream_balls = int(input())

calculate_purchase_opportunity(ice_cream_balls)
