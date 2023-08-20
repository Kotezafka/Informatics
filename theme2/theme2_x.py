class Cow:
    def __init__(self, number_of_cows):
        self.number_of_cows = number_of_cows

    def declension_of_nouns(self):
        if self.number_of_cows > 11 and self.number_of_cows < 21:
            print(self.number_of_cows, 'korov')
        else:
            if self.number_of_cows % 10 == 0:
                print(self.number_of_cows, 'korov')

            if self.number_of_cows % 10 == 1:
                if (self.number_of_cows > 10 and self.number_of_cows < 12):
                    print(self.number_of_cows, 'korov')
                else:
                    print(self.number_of_cows, 'korova')

            if self.number_of_cows % 10 > 1 and self.number_of_cows % 10 < 5:
                print(self.number_of_cows, 'korovy')

            if self.number_of_cows % 10 > 4:
                print(self.number_of_cows, 'korov')




def calculate_declension_of_nouns(number_of_cows):
    num = Cow(number_of_cows)

    num.declension_of_nouns()


number_of_cows = int(input())

calculate_declension_of_nouns(number_of_cows)
