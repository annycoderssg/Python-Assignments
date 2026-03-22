# Abstract Classes and Abstract Methods
#
# Concepts demonstrated:
#   abc.ABC         : base class for abstract classes
#   @abstractmethod : forces subclasses to implement the method
#   Abstract class  : cannot be instantiated directly
#   Concrete class  : implements all abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, strBrand, strModel, intYear):
        self.strBrand = strBrand
        self.strModel = strModel
        self.intYear  = intYear

    # Abstract methods — must be implemented by every subclass
    @abstractmethod
    def FuelType(self):
        pass

    @abstractmethod
    def MaxSpeed(self):
        pass

    # Concrete method — shared by all subclasses
    def Display(self):
        print("Brand     :", self.strBrand)
        print("Model     :", self.strModel)
        print("Year      :", self.intYear)
        print("Fuel Type :", self.FuelType())
        print("Max Speed :", self.MaxSpeed(), "km/h")


class Car(Vehicle):
    def __init__(self, strBrand, strModel, intYear, intDoors):
        super().__init__(strBrand, strModel, intYear)
        self.intDoors = intDoors

    def FuelType(self):
        return "Petrol"

    def MaxSpeed(self):
        return 180

    def Display(self):
        print("--- Car ---")
        super().Display()
        print("Doors     :", self.intDoors)


class ElectricCar(Vehicle):
    def __init__(self, strBrand, strModel, intYear, intRange):
        super().__init__(strBrand, strModel, intYear)
        self.intRange = intRange

    def FuelType(self):
        return "Electric"

    def MaxSpeed(self):
        return 250

    def Display(self):
        print("--- Electric Car ---")
        super().Display()
        print("Range     :", self.intRange, "km per charge")


class Truck(Vehicle):
    def __init__(self, strBrand, strModel, intYear, fltPayload):
        super().__init__(strBrand, strModel, intYear)
        self.fltPayload = fltPayload

    def FuelType(self):
        return "Diesel"

    def MaxSpeed(self):
        return 120

    def Display(self):
        print("--- Truck ---")
        super().Display()
        print("Payload   : %.1f tonnes" % self.fltPayload)


def main():
    # Trying to instantiate abstract class — will raise TypeError
    try:
        objVehicle = Vehicle("Generic", "Model", 2020)
    except TypeError as e:
        print("Cannot instantiate abstract class:", e)

    print()

    objCar         = Car("Toyota", "Corolla", 2022, 4)
    objElectricCar = ElectricCar("Tesla", "Model 3", 2023, 570)
    objTruck       = Truck("Tata", "Prima", 2021, 25.0)

    arrVehicles = [objCar, objElectricCar, objTruck]
    for objV in arrVehicles:
        objV.Display()
        print()

if __name__ == "__main__":
    main()
