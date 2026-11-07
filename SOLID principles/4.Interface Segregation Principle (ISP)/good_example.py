# we will segegrate the abstract methods so class that do not require them are not forced to inherit them

from abc import ABC, abstractmethod

class Eatable(ABC):
    def eat(self):
        pass

class Workable(ABC):
    def work(self):
        pass

class Employee(Workable, Eatable):
    def eat(self):
        print('employee eats')

    def work(self):
        print('employee works')

class Robot(Workable):
    def work(self):
        print('Robot works')

robot_1 = Robot()
robot_1.work()
