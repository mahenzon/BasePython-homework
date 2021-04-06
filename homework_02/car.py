"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework02.base import Vehicle
from homework02.engine import Engine

class Car(Vehicle):
    """ defaults """
    engine = None


    def set_engine(self, engine):

        self.engine = engine
