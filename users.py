

class UserDistribution:

    def __init__(self, number, exponent_index, max_salary):
        self.number = number
        self.exponent_index = exponent_index
        self.max_salary = max_salary

        self.norm_coeff = number * (exponent_index + 1) / max_salary ** (exponent_index + 1)

    def get(self, price):
        return round(self.norm_coeff * price ** self.exponent_index)

