from work_place import WorkPlace, Consts
from math import *
class School(WorkPlace):

    
    def __init__(self, name):
        super().__init__(name)
        self.expertise = "school"

    def calc_capacity(self):
        self.capacity = int(floor(sqrt(self.level)))
    
    def calc_costs(self):
        return  Consts.BASE_PLACE_COST * int(sqrt(self.level))