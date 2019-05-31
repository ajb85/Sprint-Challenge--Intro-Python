# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    #base class
    # def __init__(vStuff)
    pass

class GroundVehicle(Vehicle):
    # Base class: Vehicle
    # def __init__(gvStuff, vStuff):
        # super().__init__(vStuff)
    pass

class Car(GroundVehicle):
    # Base class: GroundVehicle
    # def __init__(cStuff, gvStuff):
        # super().__init__(gvStuff)
    pass

class Motorcycle(GroundVehicle):
    # Base class: GroundVehicle
    # def __init__(mcStuff, gvStuff):
        # super().__init__(gvStuff)
    pass

class FlightVehicle(Vehicle):
    # Base class: Vehicle
    # def __init__(fvStuff, vStuff):
        # super().__init__(vStuff)
    pass

class Airplane(FlightVehicle):
    # Base class: FlightVehicle
    # def __init__(apStuff, fvStuff):
        # super().__init__(fvStuff)
    pass

class Starship(FlightVehicle):
    # Base class: FlightVehicle
    # def __init__(ssStuff, fvStuff):
        # super().__init__(fvStuff)
    pass

# For fun
class Enterprise(Starship):
    # Base class: Starship
    # def __init__(eStuff, ssStuff):
        # super().__init__(ssStuff)
    pass