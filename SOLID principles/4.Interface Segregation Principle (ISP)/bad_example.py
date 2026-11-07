# It states that : There should be no function in a class that doesn't serve it
from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass

class Employee(Worker):
    def eat(self):
        print('worker eats')

    def work(self):
        print('worker works')

class Robot(Worker):
    def eat(self):
        raise Exception('Error : Robots do not eat')

    def work(self):
        print('Robot works')

robot_1 = Robot()
robot_1.eat()