class Number:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def number_of_ways_to_choose_K_from_N_different_items(self):
        fact1 = 1
        fact2 = 1
        fact3 = 1
        for i in range(1, self.n + 1):
            fact1 *= i

        for i in range(1, self.k + 1):
            fact2 *= i

        difference = self.n - self.k
        for i in range(1, difference + 1):
            fact3 *= i

        c = fact1 / (fact2 * fact3)
        print(int(c))


def calculate_number_of_ways_to_choose_K_from_N_different_items(n, k):
    num = Number(n, k)

    num.number_of_ways_to_choose_K_from_N_different_items()


n = int(input())
k = int(input())

calculate_number_of_ways_to_choose_K_from_N_different_items(n, k)
