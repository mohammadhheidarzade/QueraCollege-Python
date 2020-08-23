import math


class Person:
    instances = []

    def __init__(self, name, age):
        Person.instances.append(self)
        self.name = name
        self.age = age
        self.level = 1
        self.job = ""
        self.work_place = None

    def do_level(self, income):
        return income*math.sqrt(self.level * self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    @staticmethod
    def calc_all():
        res = 0
        for person in Person.instances:
            res += person.calc()
        return res
    
    def get_job(self):
        return self.job
    
    def upgrade(self):
        self.level += 1
