from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload


class Vehicle(ABC):
    """ defaults """
    weight = 1000
    started = False
    fuel = 50
    fuel_consumption = 10 # per 100 km


    def __init__(self, weight, fuel, fuel_consumption):

        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def started(self):

        if self.started is True:
            return self.started
        else:
            if self.fuel > 0:
                self.started = True
                return self.started
            else:
                raise(LowFuelError)
                return False


    def move(self, distance):

        if self.fuel*(100/self.fuel_consumption) > distance:
            return True
        else:
            raise(NotEnoughFuel)
            return False
