import math


class UserDistribution:

    def __init__(self, number, exponent_index, max_salary):
        self.number = number
        self.exponent_index = exponent_index
        self.max_salary = max_salary
        self.min_salary = 0.9

        self.norm_coeff = (number * (1 - exponent_index)) / (max_salary ** (1 - exponent_index) -
                                                              self.min_salary ** (1 - exponent_index))
        # self.norm_coeff = (exponent_index * number) / (math.exp(-exponent_index * self.min_salary) -
        #                                                math.exp(-exponent_index * self.max_salary))

    def get(self, price):
        return self.norm_coeff * price ** (-self.exponent_index)
        # return round(self.norm_coeff * math.exp(-self.exponent_index * price))

    def distrib(self, price_step):
        def distrib_gen():
            for price in range(1, self.max_salary, price_step):
                yield (price, self.get(price))
        return distrib_gen()

