from person import *

class Teacher(Person):
    
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "teacher"
    # Consts.MIN_AGE  Consts.AGE_MUL
    def get_price(self):
        return int(Consts.BASE_PRICE[self.job] - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)

    def calc_life_cost(self):
        return int(Consts.BASE_COST[self.job] + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)
    
    def calc_income(self):
        return int(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] - \
            (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)