import unittest, math
from person import *
from worker import *
from teacher import *
from engineer import *

class ScoreListTest(unittest.TestCase):

    def test_a_scenario_for_worker(self):
        worker = Worker("amir", 18)
        self.assertEqual(worker.job, "worker")
        self.assertEqual(worker.level, 1)
        self.assertEqual(worker.name, "amir")
        self.assertEqual(worker.age, 18)

        self.assertEqual(int(Consts.BASE_PRICE['worker'] * Consts.MIN_AGE / 18), worker.get_price())

        self.assertEqual(int(Consts.BASE_COST['worker'] / Consts.MIN_AGE * 18), worker.calc_life_cost())

        class WorkPlace:
            def get_expertise(self):
                return self.expertise
        worker.work_place = WorkPlace()
        worker.work_place.expertise = 'mine'

        self.assertEqual(int(Consts.BASE_INCOME['worker']['mine'] * Consts.MIN_AGE / 18), worker.calc_income())

    def test_a_scenario_for_teacher(self):
        teacher = Teacher("niloo", 19)
        self.assertEqual(teacher.job, "teacher")
        self.assertEqual(teacher.level, 1)
        self.assertEqual(teacher.name, "niloo")
        self.assertEqual(teacher.age, 19)

        self.assertEqual(int(Consts.BASE_PRICE['teacher'] - (19 - Consts.MIN_AGE) * Consts.AGE_MUL), teacher.get_price())

        self.assertEqual(int(Consts.BASE_COST['teacher'] + (19 - Consts.MIN_AGE) * Consts.AGE_MUL), teacher.calc_life_cost())

        class WorkPlace:
            def get_expertise(self):
                return self.expertise
        teacher.work_place = WorkPlace()
        teacher.work_place.expertise = 'mine'

        self.assertEqual(int(Consts.BASE_INCOME['teacher']['mine'] - (19 - Consts.MIN_AGE) * Consts.AGE_MUL), teacher.calc_income())

    def test_a_scenario_for_engineer(self):
        engineer = Engineer("yes! i'm an engineer", 37)
        self.assertEqual(engineer.job, "engineer")
        self.assertEqual(engineer.level, 1)
        self.assertEqual(engineer.name, "yes! i'm an engineer")
        self.assertEqual(engineer.age, 37)

        self.assertEqual(int(Consts.BASE_PRICE['engineer'] * math.sqrt(Consts.MIN_AGE/37)), engineer.get_price())

        self.assertEqual(int(Consts.BASE_COST['engineer'] * math.sqrt(37/Consts.MIN_AGE)), engineer.calc_life_cost())

        class WorkPlace:
            def get_expertise(self):
                return self.expertise
        engineer.work_place = WorkPlace()
        engineer.work_place.expertise = 'mine'

        self.assertEqual(int(Consts.BASE_INCOME['engineer']['mine'] * math.sqrt(Consts.MIN_AGE/37)), engineer.calc_income())

