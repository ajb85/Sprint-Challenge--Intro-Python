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

class FlightVehicle(Vehicle):
    # Base class: Vehicle
    # def __init__(fvStuff, vStuff):
        # super().__init__(vStuff)
    pass

class Starship(FlightVehicle):
    # Base class: FlightVehicle
    # def __init__(ssStuff, fvStuff):
        # super().__init__(fvStuff)
    pass

    