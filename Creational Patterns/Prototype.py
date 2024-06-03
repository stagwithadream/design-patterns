"""
Prototype Design pattern:

    Prototype design pattern is a creational design pattern that lets you copy existing objects without making your
    code dependent on their classes.

    This happens a lot when your code works with objects passed to you from 3rd-party code via some interface. The
    concrete classes of these objects are unknown, and you couldn’t depend on them even if you wanted to.

    Examples where this can be used:
    1. Long config objects
    2.
"""
from abc import ABC, abstractmethod


# Abstract Prototype class/ Interface
class Vehicle(ABC):
    def __init__(self, config=None):
        if config:
            self.owner = config.owner
            self.color = config.color
            self.engine = config.engine
        else:
            self.owner = None
            self.color = None
            self.engine = None

    @abstractmethod
    def clone(self):
        pass


# Concrete Prototype class/ Implementation
class Car(Vehicle):
    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.wheels = source.wheels
            self.topSpeed = source.topSpeed
        else:
            self.wheels = None
            self.topSpeed = None

    def clone(self):
        return Car(self)


# Concrete Prototype class/ Implementation
class Truck(Vehicle):
    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.towingCapacity = source.towingCapacity
            self.towHook = source.towHook
        else:
            self.towingCapacity = None
            self.towHook = None

    # here rather than calling constructor with self we can add more rules as well, according to the need.
    def clone(self):
        return Truck(self)


if __name__ == "__main__":
    vehicles = []

    bmw = Car()
    bmw.owner = "John"
    bmw.color = "Red"
    bmw.engine = "V8"
    bmw.wheels = 4
    bmw.topSpeed = 200
    vehicles.append(bmw)

    bmw2 = bmw.clone()
    vehicles.append(bmw2)

    print(vehicles)
    print(vehicles[0].owner)
    print(vehicles[1].owner)
