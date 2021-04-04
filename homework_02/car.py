"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine

class Car(Vehicle):
    """ defaults """
    engine = None


    def set_engine(self, engine):

        self.engine = engine
