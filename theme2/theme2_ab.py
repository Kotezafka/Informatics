class Oranges:
    def __init__(self, number_of_oranges):
        self.number_of_oranges = number_of_oranges

    def declension_of_nouns(self):
        if self.number_of_oranges > 11 and self.number_of_oranges < 21:
            print(self.number_of_oranges, 'bochek')
        elif self.number_of_oranges % 100 >= 11 and self.number_of_oranges % 100 < 21:
            print(self.number_of_oranges, 'bochek')
        else:
            if self.number_of_oranges % 10 == 0:
                print(self.number_of_oranges, 'bochek')

            if self.number_of_oranges % 10 == 1:
                if self.number_of_oranges == 11:
                    print(self.number_of_oranges, 'bochek')
                else:
                    print(self.number_of_oranges, 'bochka')

            if self.number_of_oranges % 10 > 1 and self.number_of_oranges % 10 < 5:
                print(self.number_of_oranges, 'bochki')

            if self.number_of_oranges % 10 > 4:
                print(self.number_of_oranges, 'bochek')


def calculate_declension_of_nouns(number_of_oranges):
    num = Oranges(number_of_oranges)

    num.declension_of_nouns()


number_of_oranges = int(input())

calculate_declension_of_nouns(number_of_oranges)
