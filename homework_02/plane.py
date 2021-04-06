"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.vehicle import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    """ defaults """
    cargo = 0
    max_cargo = 10000


    def __init__(self, max_cargo):

        self.max_cargo = max_cargo


    def load_cargo(self, new_cargo):

        if self.cargo + new_cargo > self.max_cargo:
            raise(CargoOverload)
            return self.cargo
        else:
            self.cargo += new_cargo
            return self.cargo


    def remove_all_cargo(self):

        last_cargo = self.cargo
        self.cargo = 0
        return self.cargo
