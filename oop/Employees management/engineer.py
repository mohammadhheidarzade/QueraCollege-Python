from person import *

from math import sqrt

class Engineer(Person):
    

    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "engineer"
    # Consts.MIN_AGE  Consts.AGE_MUL
    def get_price(self):
        return int(Consts.BASE_PRICE[self.job] * sqrt(Consts.MIN_AGE/self.age))

    def calc_life_cost(self):
        return int(Consts.BASE_COST[self.job] * sqrt(self.age/Consts.MIN_AGE))

    def calc_income(self):
        return int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * sqrt(Consts.MIN_AGE/self.age))