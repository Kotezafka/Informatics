class Avosika:
    def __init__(self, amount_peoples, amount_apples):
        self.amount_peoples = amount_peoples
        self.amount_apples = amount_apples

    def division(self):
        a = self.amount_apples // self.amount_peoples
        return a


def popolam(amount_peoples, amount_apples):
    avos = Avosika(amount_peoples, amount_apples)

    return avos.division()
